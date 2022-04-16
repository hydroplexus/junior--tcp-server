#!/usr/bin/python

from ctypes import addressof
from logging import exception
import sys
import argparse
import socketserver
import re
from tokenize import group
    
#TODO: make server class more integrated to os
class Server(socketserver):
    #TODO: move Server::HRecieve to external file
    class HRecieve(socketserver.BaseRequestHandler):
        def __init__(self, Server):
            super().__init__()
            self.setup=Server.setup
            self.finish=Server.finish
            self.handle=Server.handle
            
    
    def __init__(self, host, port):
        super().__init__((host, port), Server.HRecieve)

    def setup(self):
        self.__pattern = re.compile(r'(?P<num>\d{4}) (?P<chn>C\d) (?P<at>\d{2}:\d{2}:\d{2}.\d)\d{2} (?P<grp>\d{2})$')
        self.__response = b''
        self.client = self.client_address[0] + ':' + str(self.client_address[1])
        logName = './results.log'
        self.logFile = open(logName, 'a')
        
    def finish(self):
        print('Client ' + self.client + ' disconnected\r\n'
                'Waiting for new one...')
        self.logFile.flush()
        self.logFile.close()
        
    def handle(self):
        accum = b''
        print('Connected client from ' + self.client + '\r\n'
                'Start recieving data...')
        while True:
            data = self.request.recv(1024)
            if not data: break
            #FIXME: strange with per character data recieving from windows telnet client 
            accum += data
            if accum.find(b'\r'):
                self.__response += accum
                accum = b''
                self.check()
                
    def check(self):
        list = self.__response.split(b'\r')
        for record in list:
            match = self.__pattern.search(record.decode('ascii'))
            if match:
                self.logger(match)
        self.logFile.flush()
        self.__response = b''
        
    def logger(self, match):
        if match.group('grp') == '00':
            confirm = 'Спортсмен, нагрудный номер ' + match.group('num') + ' прошёл отсечку ' + match.group('chn') + ' в "' + match.group('at') + '"'
            print(confirm)
        self.logFile.write(match.group(0) + '\r\n')
   
          
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='')
    parser.add_argument('-p', '--port', type=int, default=0)
    
    args = parser.parse_args(sys.argv[1:])
    address = re.match('^(([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$', args.address)
    if address:
        host = address.group(0)
    else:
        host = '0.0.0.0'
        print('Server address must be in format X.X.X.X, where X must be in range 0..255\r\n'
              'Server will try to listen whole interfaces')
    port = args.port
    if not port in range(1000, 65535):
        sys.exit('Port number must be in range 1000-65535.\r\n')
    
    try:
        server = Server(host, port)
        print('Server starts at {}:{}'.format(host, port))
        server.serve_forever()
    except Exception as exeption:
        print(exception)
    

if __name__ == "__main__":
    main()
