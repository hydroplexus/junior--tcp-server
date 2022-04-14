#!/usr/bin/python

import socketserver
import re
    
class JResponse():
    __pattern = re.compile('[0-9]')
    
    def __init__(self, data=''):
        self.__data = data
    
    def check(self, data):
        error = None
        text = None
        self.__data += data
        return (error, text)
        
        
    def convert(self):
        pass
    
    
class JServer(socketserver.TCPServer):
    
    class HRecieve(socketserver.BaseRequestHandler):
        __response = JResponse()
        def handle(self):
            data = '0'
            while True:
                incom = self.request.recv(24)
                if not data: break
                check = __response.check(data)
                match check[0]:
                    case none: break
                    case
                
                print(b'\r\n' in data)
                #self.request.send()
            
            
    def __init__(self, host='0.0.0.0', port=5000):
        try:
            super().__init__((host, port), self.HRecieve)
        except Exception as exception:
            print(exception)
        finally:
            print('Server succesfully started at {}:{}'.format(host, port))
          
          
def main() -> None:
    host = '0.0.0.0'
    port = 5000
    log_dir = 'log'
    log_err = 'err.log'
    log_result = 'result.log'
    
    server = JServer(host, port)
    server.serve_forever()
     
        
if __name__ == "__main__":
    main()
