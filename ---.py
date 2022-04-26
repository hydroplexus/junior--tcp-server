import threading
import multiprocessing
import queue
import socketserver
import time


class Super:
    @classmethod
    def inheritants(cls) -> map:
        list = cls.__subclasses__()
        return {sub.__name__ : sub for sub in list}
    
    def __init__(self):
        print(Super.inheritants())
    
class Sub1(Super):
    def tell():
        print('i am Sub1')

class Sub2(Super):
    def tell():
        print('i am Sub2')

print(Super.inheritants())