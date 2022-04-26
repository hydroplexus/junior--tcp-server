
import socketserver
import threading

import JMessage

class JServer:
    class JServerError(Exception):
        __types = {
            0 : 'No such ErrorNumber!.',
            1 : 'Address is not in IPv4.',
            2 : 'Port must be a number.',
            3 : 'Port must be in range 0-65535.',
            4 : 'Access to ports in range 0-1000 granted for root only.',
            5 : 'Socket is already in use.'
            }
        
        def __init__(self, errNum: int) -> None:
            self.__errNum = errNum
            
        def __str__(self) -> str:
            return type(self).__types(self.__errNum)
        
    class HRecieve(socketserver.StreamRequestHandler):
        def setup(self) -> None:
            super().setup()
            ...
            
        def finish(self) -> None:
            ...
            
        async def handle(self) -> None:
            while True:
                raw = self.rfile.readline(1024)
                if not raw: break
                await JServer.MsgRaw(self, raw).spool() 
    
    def __init__(self, interface: str, port: int) -> None:
        try:
            self.__srv = socketserver.TCPServer((interface, port), self.HRecieve)
        except PermissionError as ex: ...
        except OSError as ex: ...
        except Exception as ex:
            raise ex
        
        self.commutate()
        self.__thrSrv = threading.Thread(target=self.__srv.serve_forever)
   
    def start(self) -> None:
        self.__thrSrv.start()
        
    def stop(self) -> None:
        self.__srv.finish()
        self.__thrSrv.stop()
        self.__rawSpooler.join()
        