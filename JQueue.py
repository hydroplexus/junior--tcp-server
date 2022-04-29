
import asyncio
import threading

class JQueueMetaSingle():
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(JQueueMetaSingle, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class JQueue(asyncio.PriorityQueue):
    def __init__(self) -> None:
        self.wrksTreshold = 4
        self.msgsTreshold = 100
        self.pollPeriod = 5
        self.workers = []
        self._addWorkers(self.wrksTreshold)
    
    async def _correctkWorkload(self) -> None:
        treshold = (self.qsize // self.msgsTreshold * self.wrksTreshold)
        if treshold > self.workers.count():
            await self._addWorkers(treshold)
        if treshold < self.workers.count():
            await self._addWorkers(treshold)
        threading.Timer(self.pollPeriod, self._correctkWorkload()).start()
    
    async def _addWorkers(self, treshold) -> None:
        for _ in range(self.workers.count(), treshold - 1):
            await self.workers.append(asyncio.create_task(self._worker(self)))
    
    async def _delWorkers(self, treshold):
        for _ in range(treshold + 1, self.workers.count()): #self.workers[treshold::]
            await self.put((0, 'kill'))
    
    async def _worker(self) -> None: ...

class QueRaw(JQueue, metaclass = JQueueMetaSingle):
    async def _worker(self):
        while True:
            msg = self.get()
            if msg == 'kill':
                self.task_done()
                break