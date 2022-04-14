#!/usr/bin/python

import socketserver
import re
    
class Server(socketserver.TCPServer):
    
    class HRecieve(socketserver.BaseRequestHandler):
        log_dir = 'log/'
        log_err = 'err.log'
        log_result = 'result.log'
        __pattern = re.compile('[0-9]')
        __response = b''
        
        def handle(self):
            accum = b''
            while True:
                data = self.request.recv(1024)
                if not data: break
                accum += data
                if accum.find(b'\r'):
                    self.__response += accum
                    print (self.__response)
                    accum = b''
                    self.check()
                    
        def check(self):
            list = self.__response.split(b'\r')
            
        def convert(self, data):
            pass
        
        def logger(self):
            pass
            
            
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
