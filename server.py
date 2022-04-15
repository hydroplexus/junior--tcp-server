#!/usr/bin/python

import sys
import argparse
import socketserver
import re
    
#TODO: make server class more integrated to os
class Server(socketserver.TCPServer):
    #TODO: move Server::HRecieve to external file
    class HRecieve(socketserver.BaseRequestHandler):
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
            
    
    def __init__(self, host='0.0.0.0', port=5000):
        try:
            super().__init__((host, port), self.HRecieve)
        except Exception as exception:
            print(exception)
        finally:
            print('Server succesfully started at {}:{}'.format(host, port))

def setParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int, default=5000)
    return parser
          
def main():
    parser = setParser()
    args = parser.parse_args(sys.argv[1:])
    if args.port < 1000:
        args.port = parser.get_default('port')
        print('Port number is low then 1000. You must be root for use it.\r\n'
              'Fallback to default ' + str(args.port))
    if not re.match('^(([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$', args.address):
        args.address = parser.get_default('address')
        print('Address must be in format X.X.X.X, where X must be in range 0..255\r\n'
              'Fallback to default 0.0.0.0')
    server = Server(args.address, args.port)
    server.serve_forever()
     
        
if __name__ == "__main__":
    main()
