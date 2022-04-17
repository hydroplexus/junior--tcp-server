#!/usr/bin/python

from socket import gaierror
import sys
import os
import argparse
import socketserver
import re
    
#TODO: make server class more integrated to os
class JServer(socketserver.TCPServer):
    class JServerError(Exception):
        pass
    #TODO: move Server::HRecieve to external file
    class HRecieve(socketserver.StreamRequestHandler):
        __client :str
        
        def setup(self) -> None:
            super().setup()
        
        def finish(self):
            self.server.connectLose(self.client)
            
        def handle(self) -> None:
            self.client = '{}:{}'.format(self.client_address[0], self.client_address[1])
            print('Connected client from {}\r\n'\
                'Start recieving data...'\
                .format(self.client))
            while True:
                data = self.rfile.readline(1024)
                if not data: break
                self.server.check(data)

    __RGX_CHECK = b'\d{4} C\d \d{2}:\d{2}:\d{2}.\d{3} \d{2}\r$'
    __RGX_CATCH = r'(\d{4}) (C\d) (\d{2}:\d{2}:\d{2}.\d)\d{2} (00)\r$'
    
    __host: str
    __port: int
    __logFileName = './results.log'
    __logFlushMax = 7
    __logBuffer = list()
    __rgxCheck = re.compile(__RGX_CHECK)
    __rgxCatch = re.compile(__RGX_CATCH)
    
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        print('Trying to bind at {}:{}...'.format(host, port))
        try:
            super().__init__((host, port), self.HRecieve)
        except TypeError as ex:
            raise self.JServerError('You must specify the port')
        except OverflowError as ex:
            raise self.JServerError('Port not in range 0-65535')
        except gaierror as ex:
            raise self.JServerError('Unable to recognize host address')
        except PermissionError as ex:
            raise self.JServerError('Port access in range 0-1000 is granted root only')
        except OSError as ex:
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
        if self.__logBuffer.__len__() >= self.__logFlushMax:
            self.flushLog()
            
    def flushLog(self) -> None:
        with open(self.__logFileName, 'a') as file:
            file.writelines('%s' % record for record in self.__logBuffer)
        self.__logBuffer.clear()
            
    def connectLose(self, client: str) -> None:
        self.flushLog()
        print('\rClient {} disconnected\r\n'\
            'Waiting for new one...'\
            .format(client))

    
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int)
    
    args = parser.parse_args(sys.argv[1:])
    host = args.host
    port = args.port
    try:
        server = JServer(host, port)
    except JServer.JServerError as ex:
        print(ex, file = sys.stderr)
        sys.exit('Module stopped by internal error')

    server.serve_forever()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\rModule stopped by KeyboardInterrupt')
