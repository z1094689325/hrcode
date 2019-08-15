#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue 
import threading
import time

class M:
    
    def __init__(self):
        
        self.q = queue.Queue(5)
        
    
    def producer(self):
        
        for i in range(20):
            
            self.q.put(i)
            
    
    def worker(self):
        
        while True :
            
            data = self.q.get()
            
            time.sleep(2)
            
            print(data)
            
            
    
    def main(self):
        
        for i in range(2):
            
            t = threading.Thread(target=self.worker)
            
            t.start()
        
        self.producer()
        
        
        
        
if __name__ == "__main__" :
    
    m = M()
    
    m.main()