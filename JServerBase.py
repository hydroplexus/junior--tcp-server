#!/usr/bin/python

import sys
import logging
import socketserver
from multiprocessing import queues

class JServerBase(socketserver.TCPServer):
    class JServerError(Exception): ...
    class HRecieve(socketserver.TCPServer):
        def setup(self) -> None:
           super().setup()
           
        def finish(self) -> None: ...
        
        def handle(self) -> None:
            while True:
                data = self.rfile.readline(1024)
                if not data: break
        
    def __init__(self, interface: str, port: int) -> None:
        self.__interface = interface
        self.__port = port
        try:
            super().__init__((interface, port), self.HRecieve)
        except PermissionError as ex:
            pass
        except OSError as ex:
            pass
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
