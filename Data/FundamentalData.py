# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:18:25 2021

@author: Gavin
"""

import FundamentalAnalysis as fa
import matplotlib.pyplot as plt


class fundamentalData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.api_key = "5460f75cb4f1f62a42c79066e3622078"
        self.companiesProfile               = fa.profile(self.ticker, self.api_key)
        self.quotes                         = fa.quote(self.ticker, self.api_key)
        self.entreprise_value               = fa.enterprise(self.ticker, self.api_key)
        self.ratings                        = fa.rating(self.ticker, self.api_key)
        self.dcf_annually                   = fa.discounted_cash_flow(self.ticker, self.api_key, period="annual")
        self.dcf_quarterly                  = fa.discounted_cash_flow(self.ticker, self.api_key, period="quarter")
        self.balance_sheet_annually         = fa.balance_sheet_statement(self.ticker, self.api_key, period="annual")
        self.balance_sheet_quarterly        = fa.balance_sheet_statement(self.ticker, self.api_key, period="quarter")
        self.income_statement_annually      = fa.income_statement(self.ticker, self.api_key, period="annual")
        self.income_statement_quarterly     = fa.income_statement(self.ticker, self.api_key, period="quarter")
        self.cash_flow_statement_annually   = fa.cash_flow_statement(self.ticker, self.api_key, period="annual")
        self.cash_flow_statement_quarterly  = fa.cash_flow_statement(self.ticker, self.api_key, period="quarter")
        self.key_metrics_annually           = fa.key_metrics(self.ticker, self.api_key, period="annual")
        self.key_metrics_quarterly          = fa.key_metrics(self.ticker, self.api_key, period="quarter")
        self.financial_ratios_annually      = fa.financial_ratios(self.ticker, self.api_key, period="annual")
        self.financial_ratios_quarterly     = fa.financial_ratios(self.ticker, self.api_key, period="quarter")
        self.growth_annually                = fa.financial_statement_growth(self.ticker, self.api_key, period="annual")
        self.growth_quarterly               = fa.financial_statement_growth(self.ticker, self.api_key, period="quarter")
        self.stock_data                     = fa.stock_data(self.ticker, period="ytd", interval="1d")
        self.stock_data_detailed            = fa.stock_data_detailed(self.ticker, self.api_key, begin="2000-01-01", end="2020-01-01")
        
        
    def getAllCompanies(self):
        print("in df format")
        return fa.available_companies(self.apiKey)
    
    def getStockData(self, interval_input = "1d"):
        return fa.stock_data(self.ticker, period="ytd", interval=interval_input)
    
    def getStockDataDetailed(self, startDate , endDate):
        return fa.stock_data_detailed(self.ticker, self.api_key)

    def documentation(self):
        return """

        self.ticker
        self.api_key 
        self.companiesProfile               
        self.quotes                         
        self.entreprise_value               
        self.ratings                        
        self.dcf_annually                   
        self.dcf_quarterly                  
        self.balance_sheet_annually         
        self.balance_sheet_quarterly        
        self.income_statement_annually      
        self.income_statement_quarterly     
        self.cash_flow_statement_annually   
        self.cash_flow_statement_quarterly  
        self.key_metrics_annually           
        self.key_metrics_quarterly          
        self.financial_ratios_annually      
        self.financial_ratios_quarterly     
        self.growth_annually                
        self.growth_quarterly               
        self.stock_data                     
        self.stock_data_detailed            
        """
        

if __name__ =="__main__":
    x = fundamentalData("AAPL")
    print(x.documentation())

