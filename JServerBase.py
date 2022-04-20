#!/usr/bin/python

import sys
import logging
from multiprocessing import queues
from socket import socketserver

class JServerBase(socketserver.TCPServer):
    class JServerError(Exception): ...
    class HRecieve(socketserver.TCPServer):
        def setup(self) -> None:
           super().setup()
        def finish(self) -> None: ...
        def handle(self) -> None:
            while True:
                data = self.rfile.readline(1024)
                if not data break
        
    def __init__(self, interface: str, port: int) -> None:
        try:
            super().__init__((interface, port), self.HRecieve)
        except PermissionError as ex:
            pass
        except OSError as ex:
            pass
        except Exception as ex:
            raise ex
        self.__interface = interface
        self.__port = port
        self.__setup()
        
    def __setup(self) -> None: ...
