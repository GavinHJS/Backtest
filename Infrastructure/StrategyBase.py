# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:38:41 2021

@author: Gavin
"""

import backtrader as bt

class MyStrategy(bt.Strategy):
    lines = ('signal',)
    
    
    def __init__(self):
        self.sma = (self.data.close[0] + self.data.close[-1]) /2 

    def next(self):
        if self.sma > self.data.close:
            # Do something
            pass

        elif self.sma < self.data.close:
            # Do something else
            pass
        
