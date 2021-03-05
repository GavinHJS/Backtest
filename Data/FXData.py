# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:33:45 2021

@author: Gavin
"""

import pandas as pd
from datetime import datetime
import yfinance as yf

class fxData():
    def __init__(self,fx,startDate , endDate , frequency):
        if len(fx) != 5:
            raise ValueError("Invalid Fx Format. Try e.g. EUR=X")
        else:
            self.fxPair = fx
            
        self.startDate = startDate
        self.endDate = endDate
        self.frequency = frequency
        
        
    def getData(self):
        historicalData = yf.Ticker(self.fxPair)
        historicalData.history()
        
        
        

if __name__ == "__main__":
    x = fxData("EUR=X" , "2020-01-01" , "2021-01-01", "1d")