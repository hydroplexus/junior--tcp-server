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
            self.logFile.close()
            
        def handle(self):
            accum = b''
            print('Connected client from ' + self.client + '\r\n'
                  'Start recieving data...')
            while True:
                data = self.request.recv(1024)
                if not data: break
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
            self.__response = b''
            
        def logger(self, match):
            if match.group('grp') == '00':
                confirm = 'Спортсмен, нагрудный номер ' + match.group('num') + ' прошёл отсечку ' + match.group('chn') + ' в "' + match.group('at') + '"'
                print(confirm)
            self.logFile.write(match.group(0))
            
    
    def __init__(self, host='0.0.0.0', port=5000):
        try:
            super().__init__((host, port), self.HRecieve)
        except Exception as exception:
            print(exception)
        finally:
            print('Server succesfully started at {}:{}'.format(host, port))

          
def main() -> None:
    server = Server()
    server.serve_forever()
     
        
if __name__ == "__main__":
    main()
