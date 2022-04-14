#!/usr/bin/python

import socket
import sys

from PySide6.QtCore import QObject

class JuniorServer(QObject):
    
    def __init__(self) -> None:
        super().__init__(parent)

def main(): -> None:
    server = JuniorServer
    server.start()
    
if __name__ == "__main__":
    main()
