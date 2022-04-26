
import asyncio
import threading

import JMessage

class JQueue(asyncio.PriorityQueue):        
    @classmethod        
    def getSubclasses(cls) -> map:
        list = cls.__subclasses__()
        return {sub.__name__ : sub for sub in list}
    
    def __init__(self) -> None:
        self.wrksTreshold = 4
        self.msgsTreshold = 100
        self.pollPeriod = 5
        self.workers = []
        self.addWorkers(self.wrksTreshold)
        
    async def checkWorkload(self) -> None:
        treshold = (self.qsize // self.msgsTreshold * self.wrksTreshold)
        if treshold > self.workers.count():
            await self.addWorkers(treshold)
        if treshold < self.workers.count():
            await self.addWorkers(treshold)
        threading.Timer(self.pollPeriod, self.checkWorkload()).start()
    
    async def addWorkers(self, treshold) -> None:
        for _ in range(self.workers.count(), treshold - 1):
            await self.workers.append(asyncio.create_task(self.worker(self)))
            
    async def delWorkers(self, treshold):
        for _ in range(treshold + 1, self.workers.count()):
            await self.put((0, 'kill'))
        
    async def worker(self) -> None: ...
            
class QueRaw(JQueue):
    async def worker(self):
        while True:
            msg = self.get()
            if msg == 'kill':
                self.task_done()
                break