
import datetime
import regex

import JServer
import JQueue

class JMessageMetaSingle(): ...

class JMessage(metaclass = JMessageMetaSingle):
    class Message:
        datetime: datetime.datetime
        timestamp: datetime.timestamp
        client: int
        raw: bytes
    
    sig = None
    rcvQueue: None
    
    def __init__(self, client, raw) -> None:
        self.message = self.Message()
        self.message.datetime = datetime.datetime.now()
        self.message.timestamp = datetime.timestamp()
        self.message.client = client
        self.message.raw = self.__class__.sig + self.raw
    
    def spool(self) -> None:
        self.__class__.rcvQueue.put(self.message.timestamp, self.message)
    
    def worker(self) -> None: ...

class MsgRaw(JMessage):
    sig = b''
    rcvQueue = JQueue.QueRaw()
    
    @staticmethod
    def check(raw) -> None: ... 

class MsgTask(JMessage):
    sig = b''
    check = regex.compile(b'\d{4} C\d \d{2}:\d{2}:\d{2}.\d{3} \d{2}\r$')
    rcvQueue = 'QueTask'