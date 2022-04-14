#!/usr/bin/python

import socketserver
    
class JData():
    def __init__(self, data='')
        self.__data=data
    
    def check(data):
        return True
        
    def convert(self):
        pass
    
    
class JServer(socketserver.TCPServer):
    
    class HRecieve(socketserver.BaseRequestHandler):
        __data = JData()
        
        def handle(self):
            self.__data = self.request.recv(1024).strip()
            if (self,__data.check)
                print("Data is alright")
            
            
    __reciever = HRecieve()
    
    def __init__(self, host='0.0.0.0', port=5000):
          super.__init__()
          self.server_bind((host, port), self.__reciever)
          
          
def main() -> None:
    host = '0.0.0.0'
    port = 5000
    reciever = HRecieve()
    server = JServer(host, port)
    server.serve_forever()
     
        
if __name__ == "__main__":
    main()
