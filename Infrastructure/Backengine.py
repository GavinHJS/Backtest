# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:07:17 2021

@author: Gavin

Note:
        Date is in YYYY-MM-DD format
"""

import backtrader as bt
import sys

sys.path.insert(1, "'D:\\Backtesting\\Data'")

from EquityData import dataPreperation

class backEngine:
    
    def __init__(self , tickerData,date1 , date2 , frequency):
        self.data = dataPreperation(tickerData , date1,date2 , frequency).getHistoricalData()
        cerebro = bt.Cerebro()


    # cerebro = bt.Cerebro()

    # data = bt.feeds.YahooFinanceCSVData(
    #     dataname=x,
    #     # Do not pass values before this date
    #     fromdate=datetime.datetime(2000, 1, 1),
    #     # Do not pass values after this date
    #     todate=datetime.datetime(2000, 12, 31),
    #     reverse=False)

    # # Add the Data Feed to Cerebro
    # cerebro.adddata(data)

    # # Set our desired cash start
    # cerebro.broker.setcash(100000.0)
    # print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # cerebro.run()

    # print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    

if __name__ =="__main__":
    x = backEngine("MSFT" , "2020-01-01" , "2021-01-01", "1d")