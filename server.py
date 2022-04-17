#!/usr/bin/python

from socket import gaierror
import subprocess
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
    
    class HJServerBridge():
        def __init__() -> None:
            pass
        
        @classmethod
        def onMatch(self, data: str) -> None:
            pass
        
        @classmethod
        def onCatch(self, data: str) -> None:
            pass
        
        def onLogFlush(self) -> None:
            pass
        
    __RGX_IPV4 = '^(([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$'
    __RGX_CHECK = r'\d{4} C\d \d{2}:\d{2}:\d{2}.\d{3} \d{2}$'
    __RGX_CATCH = r'(\d{4}) (C\d) (\d{2}:\d{2}:\d{2}.\d)\d{2} (00)$'
    
    __host: str
    __port: int
    __logFileName = './results.log'
    __logFlushMax = 7
    __logBuffer = list()
    __rgxIPv4 = re.compile(__RGX_IPV4)
    __rgxCheck = re.compile(__RGX_CHECK)
    __rgxCatch = re.compile(__RGX_CATCH)
    __isBridged = False
    __hBridge: HJServerBridge = None
    
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
            data = 'Спортсмен, нагрудный номер {}, прошёл отсечку {} в "{}"'\
                .format(catch.group(1), catch.group(2), catch.group(3))
            print(data)
            self.__hBridge.onCatch(data)
    
    def logger(self, match: str) -> None:
        self.__logBuffer.append('{}\r\n'.format(match))
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
    
    def setBridge(self, bridge: HJServerBridge) -> None:
        self.__hBridge = bridge
        self.__isBridged = True

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int)
    
    args = parser.parse_args(sys.argv[1:])
    host = args.host
    port = args.port
    try:
        server = JServer(host, port)
    except Exception as ex:
        print(ex)
        sys.exit('Module stopped by internal error')

    server.serve_forever()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\rModule stopped by KeyboardInterrupt')
