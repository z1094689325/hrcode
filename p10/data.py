#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open('./data.json','r', encoding='utf-8') as f:
    
    data = json.loads(f.read())

li = []

def x(a):
    
    if type(a) != dict:
        
        return 
    
    for i,j in a.items():
        
        if type(j) == int :
            
            li.append({i:j})
            
        elif type(j) == dict:
            
            x(j)
            
        elif type(j) == list:
            
            for k in j:
                
                x(k)
                

if __name__ == "__main__" :
    
    
    x(data)
    
    li.sort(key=lambda x:list(x.values())[0])
    
    with open('./p2.txt','a',encoding='utf-8') as f:
        
        f.write(str(li))