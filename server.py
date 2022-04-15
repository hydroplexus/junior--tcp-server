#!/usr/bin/python

import sys
import argparse
import socketserver
import re
    
class Server(socketserver.TCPServer):
    
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
                #Эта странность от того, что клиент telnet на Windows отправляет символы по одному по мере набора
                #махинации с его настройками не помогли
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
    parser.add_argument('-a', '--address', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int, default=5000)
    return parser
          
def main():
    parser = setParser()
    args = parser.parse_args(sys.argv[1:])
    if args.port < 1000:
        args.port = parser.get_default('port')
        print('Port number is low then 1000. You must be root for use it.\r\n'
              'Fallback to default ' + str(args.port))
    if None == re.match('\d{1-3}.\d{1-3}.\d{1-3}.\d{1-3}', args.address):
        args.address = parser.get_default('address')
        print('Address must be in format XXX.XXX.XXX.XXX, where X is digest from 0 to 9\r\n'
              'Fallback to default 0.0.0.0')
    server = Server(args.address, args.port)
    server.serve_forever()
     
        
if __name__ == "__main__":
    main()
