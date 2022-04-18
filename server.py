#!/usr/bin/python

from socket import gaierror
import sys
import os
import signal
import argparse
import socketserver
import re
    
#TODO: make server class more integrated to os
class JServer(socketserver.TCPServer):
    class JServerError(Exception):
        pass
    #TODO: move Server::HRecieve to external file
    class HRecieve(socketserver.StreamRequestHandler):
        
        def setup(self) -> None:
            super().setup()
            self.__client = '{}:{}'.format(self.client_address[0], self.client_address[1])
            print('Connected client from {}\r\n'\
                'Start recieving data...'\
                .format(self.__client))
        
        def finish(self) -> None:
            self.server.connectLose(self.__client)
            
        def handle(self) -> None:
            
            while True:
                data = self.rfile.readline(1024)
                if not data: break
                self.server.check(data)

    __RGX_CHECK = b'\d{4} C\d \d{2}:\d{2}:\d{2}.\d{3} \d{2}\r$'
    __RGX_CATCH = r'(\d{4}) (C\d) (\d{2}:\d{2}:\d{2}.\d)\d{2} (00)\r$'
    
    __host: str
    __port: int
    __LOG_FILE_NAME = './results.log'
    __LOG_FLUSH_MAX = 3
    __logBuffer = list()
    __rgxCheck = re.compile(__RGX_CHECK)
    __rgxCatch = re.compile(__RGX_CATCH)
    
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        print(f'Trying to bind at {host}:{port}...')
        try:
            super().__init__((host, port), self.HRecieve)
        except TypeError as ex:
            print(f'{type(ex).__name__}: {ex}')
            raise self.JServerError('You must specify both of address:port')
        except OverflowError as ex:
            print(f'{type(ex).__name__}: {ex}')
            raise self.JServerError('Port not in range 0-65535')
        except gaierror as ex:
            print(f'{type(ex).__name__}: {ex}')
            raise self.JServerError('Unable to recognize host address')
        except PermissionError as ex:
            print(f'{type(ex).__name__}: {ex}')
            raise self.JServerError('Port access in range 0-1000 is granted root only')
        except OSError as ex:
            print(f'{type(ex).__name__}: {ex}')
            raise self.JServerError('Address is alredy in use')
        except Exception as ex:
            raise ex
        
        print('Server started. Waiting for clients...')
            
    def check(self, data :bytes) -> None:
            for record in self.__rgxCheck.findall(data):
                record = str(record, 'ascii')
                self.logger(record)
                self.catch(record)
            
    def catch(self, match: str) -> None:
        catch = self.__rgxCatch.match(match)
        if catch:
            data = 'Спортсмен, нагрудный номер {}, прошёл отсечку {} в "{}"'\
                .format(catch.group(1), catch.group(2), catch.group(3))
            print(data)
    
    def logger(self, match: str) -> None:
        self.__logBuffer.append(match)
        if self.__logBuffer.__len__() >= self.__LOG_FLUSH_MAX:
            self.flushLog()
            
    def flushLog(self) -> None:
        with open(self.__LOG_FILE_NAME, 'a') as file:
            file.writelines('%s' % record for record in self.__logBuffer)
        self.__logBuffer.clear()
            
    def connectLose(self, client: str) -> None:
        self.flushLog()
        print(f'Client {client} disconnected\r\n'\
            'Waiting for new one...')

 
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', type=str)
    parser.add_argument('-p', '--port', type=int)
    
    args = parser.parse_args(sys.argv[1:])
    host = args.host
    port = args.port
    try:
        server = JServer(host, port)
    except JServer.JServerError as ex:
        print(f'{type(ex).__name__}: {ex}')
        sys.exit('Module stopped by internal error')
    except Exception as ex:
        print(f'{type(ex).__name__}: {ex}')

    server.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\rModule stopped by KeyboardInterrupt')

