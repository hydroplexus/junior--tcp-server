#!/usr/bin/python

from socket import gaierror
import sys
import os
import argparse
import socketserver
import re
    
#TODO: make server class more integrated to os
class JServer(socketserver.TCPServer):
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
                
    class JServerError(Exception): pass
        
    __LOG_FILE = './results.log'
    __LOG_FLUSH_MAX = 7
    __RGX_IPV4 = '^(([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$'
    __RGX_CHECK = r'\d{4} C\d \d{2}:\d{2}:\d{2}.\d{3} \d{2}$'
    __RGX_CATCH = r'(\d{4}) (C\d) (\d{2}:\d{2}:\d{2}.\d)\d{2} (00)$'
    
    __host: str
    __port: int
    __logBuffer = list()
    __rgxIPv4 = re.compile(__RGX_IPV4)
    __rgxCheck = re.compile(__RGX_CHECK)
    __rgxCatch = re.compile(__RGX_CATCH)
    
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        try:
            super().__init__((host, port), self.HRecieve)
        except OverflowError as ex:
            raise self.JServerError('Port not in range 0-65535')
        except gaierror as ex:
            raise self.JServerError('Unable to recognize host address')
        except PermissionError as ex:
            raise self.JServerError('Access to ports in range 0-1000 granted root only')
        except OSError as ex:
            raise self.JServerError('Address alredy in use')
        except Exception as ex:
            raise ex
        
        print('Server started at {}:{}\r\n'\
            'Waiting for clients...'\
            .format(host, port))
            
    def check(self, data :bytes) -> None:
            list = data.split(b'\r')
            for record in list:
                check = self.__rgxCheck.search(record.decode('ascii'))
                if check:
                    self.logger(check.group(0))
                    self.catch(check.group(0))
            
    def catch(self, match: str) -> None:
        catch = self.__rgxCatch.match(match)
        if catch:
            print('Спортсмен, нагрудный номер {}, прошёл отсечку {} в "{}"'\
                .format(catch.group(1), catch.group(2), catch.group(3)))
    
    def logger(self, match: str) -> None:
        self.__logBuffer.append('{}\r\n'.format(match))
        if self.__logBuffer.__len__() >= self.__LOG_FLUSH_MAX:
            self.flushLog()
            
    def flushLog(self) -> None:
        logFile = open(self.__LOG_FILE, 'a')
        for record in self.__logBuffer:
            logFile.write(record)
        self.__logBuffer.clear()
        logFile.flush()
        os.fsync(logFile.fileno())
        logFile.close()
            
    def connectLose(self, client: str) -> None:
        self.flushLog()
        print('\rClient {} disconnected\r\n'\
            'Waiting for new one...'\
            .format(client))
#HELPERS:
    

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int)
    #parser.add_argument('-h', '--help')
    
    args = parser.parse_args(sys.argv[1:])
    host = args.host
    port = args.port
    try:
        server = JServer()
    except Exception as ex:
        print(ex)
        sys.exit('Module stopped by internal error')

    server.serve_forever()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\rModule stopped by KeyboardInterrupt')
