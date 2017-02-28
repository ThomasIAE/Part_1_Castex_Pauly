import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt  # Import matplotlib
import matplotlib
import numpy as np

#Create dataframes for each stock from the 01/01/2005 to 31/12/2015
start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 12, 31)
Google = web.DataReader("GOOGL", 'yahoo', start, end)
Apple = web.DataReader("AAPL", 'yahoo', start, end)
Yahoo = web.DataReader("YHOO", 'yahoo', start, end)
AmEx = web.DataReader("AXP", 'yahoo', start, end)
Exxon = web.DataReader("XOM", 'yahoo', start, end)
Coca = web.DataReader("KO", 'yahoo', start, end)
Nokia = web.DataReader("NOK", 'yahoo', start, end)
MorganStanley = web.DataReader("MS", 'yahoo', start, end)
IBM = web.DataReader("IBM", 'yahoo', start, end)
FedEx = web.DataReader("FDX", 'yahoo', start, end)

#Drop unecessary columns of the data and only keep the 'High' column as price
Apple.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
Google.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
Yahoo.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
AmEx.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
Exxon.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
Coca.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
Nokia.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
MorganStanley.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
IBM.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)
FedEx.drop(['Open', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1, inplace=True)

#FedEx["High"].plot(grid=True)  #Plot the price of the company you want
#plt.show()

#Create a general dataframe for all stock prices
Stocks = pd.DataFrame({"AAPL": Apple["High"],
                       "GOOGL": Google["High"],
                       "YHOO":Yahoo["High"],
                       "AXP":AmEx["High"],
                       "XOM":Exxon["High"],
                       "KO": Coca["High"],
                       "NOK":Nokia["High"],
                       "MS":MorganStanley["High"],
                       "IBM": IBM["High"],
                       "FDX": FedEx["High"]})
#print(Stocks)
stock_return = Stocks.apply(lambda x: x / x[0])
#print(stock_return) #print the stock returns
stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
#plt.show() #show the plot of the returns

#the same can be done with the changes in stock prices rather than return, with the log
stock_change = Stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))
stock_change.plot(grid = True).axhline(y = 0, color = "black", lw = 2)
#plt.show()