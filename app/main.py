# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:51:16 2021

@author: Gavin
"""
import sys
sys.path.insert(0, "..\\Backtest\\Data")
sys.path.insert(1, "..\\Backtest\\Infrastructure")

from Backengine import backEngine
from EquityData import dataPreperation

x =backEngine("AAPL" , "2020-01-01" , "2021-01-01", "1d" , 1000)
x.activate()
