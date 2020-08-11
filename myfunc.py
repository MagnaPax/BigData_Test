# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:32:34 2020

@author: Kosmo_25
"""


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b



class Calc:
    def __init__(self):
        self.result=0
        
    def cadd(self,num):
        self.result+=num
        return self.result
    
    def cminus(self, num):
        self.result-=num
        return self.result
    
    def cmul(self, num):
        self.result*=num
        return self.result
    
    def cdiv(self, num):
        if num==0:
            return 0
        else:
            self.result/=num
            return self.result
        