# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:07:17 2021

@author: Gavin

Note:
        Date is in YYYY-MM-DD format
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import backtrader as bt
import sys
import datetime
import matplotlib.pyplot as plt

sys.path.insert(1, "..\\Backtest\\Data")

from EquityData import dataPreperation
import plotly

class backEngine:
    
    def __init__(self , tickerData,date1 , date2 , frequency , notional ):
        self.data       = dataPreperation(tickerData , date1,date2 , frequency).getHistoricalData()
        self.notional   = notional 
        
        
    def setEngine(self):
        self.cerebro     = bt.Cerebro()
        data             = bt.feeds.PandasData(dataname = self.data) 
        self.cerebro.adddata(data)
        self.cerebro.broker.set_cash(self.notional)
        
    def runEngine(self):
        print('Starting Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
        self.cerebro.run()
        print('Final Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
        
    def activate(self):
        self.setEngine()
        self.runEngine()
        
if __name__ =="__main__":
    x = backEngine("MSFT" , "2020-01-01" , "2021-01-01", "1d" , 1000)
    x.activate()
    
    
    
    