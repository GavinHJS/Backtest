import pandas as pd
import yfinance as yf
import datetime

class dataPreperation:
    
    def __init__(self,tickerData,date1 , date2 , frequency):
        
        self.checkDates(date1, date2)
        self.ticker     = tickerData
        self.startDate  = date1
        self.endDate    = date2
        self.frequency  = frequency
        
    def checkDates(self,firstDate , secondDate):
        firsDate    = datetime.datetime.strptime(firstDate, "%Y-%m-%d")
        secondDate  = datetime.datetime.strptime(secondDate, "%Y-%m-%d")
        if firsDate > secondDate:
            raise ValueError("Start date is later than end date")
        
        
    def getHistoricalData(self):
        historicalData = yf.Ticker(self.ticker)
        mainData = historicalData.history(period = self.frequency,
                                               start  = self.startDate,
                                               end    = self.endDate)
        return mainData
        

if __name__ == "__main__":
    x = dataPreperation("MSFT" , "2020-01-01" , "2021-01-01", "1d")



    

        
    
    
    
    