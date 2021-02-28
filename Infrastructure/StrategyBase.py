# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:38:41 2021

@author: Gavin
"""

import backtrader as bt
import backtrader.indicator as btind
class MyStrategy(bt.Strategy):
    lines = ('signal',)
    

    def __init__(self):
        self.sma = btind.SimpleMovingAverage(period = 15)
        print(self.sma)
        
            
    def next(self):
        # if self.data.close[0]> self.sma:
        #     print("sheetboi")
        print('Close:' , self.data.close[0])
