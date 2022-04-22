#!/usr/bin/python

import sys
import logging
import socketserver
from multiprocessing import queues

class JServerBase(socketserver.TCPServer):
    class JServerError(Exception): ...
    class HRecieve(socketserver.TCPServer):
        def __init__(self, server, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.__counter: int
            self.__server = server
            
        def setup(self) -> None:
           super().setup()
           self.__counter =  0
           
        def finish(self) -> None: ...
        
        def handle(self) -> None:
            while True:
                data = self.rfile.readline(1024)
                if not data: break
                self.__counter += 1
                ...
        
    def __init__(self, interface: str, port: int) -> None:
        self.__interface = interface
        self.__port = port
        try:
            super().__init__((interface, port), self.HRecieve)
        except PermissionError as ex: ...
        except OSError as ex: ...
        except Exception as ex:
            raise ex
        self.__setup()
        
    def __setup(self) -> None:
        #vars
        self.__address: str
        self.__port: int
        #queues and workers
        self.__qRawData = queues.Queue()
        self.__qMatchedData = queues.Queue()
        self.__wRDMatcher()
        self.__wMDChecker()
        
    def start() -> None: ...
    def setLogFile() -> None: ...
    def getData(data: bytes) -> None: ...
