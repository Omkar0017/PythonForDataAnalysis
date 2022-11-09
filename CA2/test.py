import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


msft = yf.Ticker("AMZN")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

print('History: ',hist)
# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends
print("Dividents: ",msft.dividends)
# show splits
msft.splits
print("Splits: ",msft.splits)

# show financials
msft.financials
print("Financials: ",msft.financials)
msft.quarterly_financials
print("Quaterly Financials: ",msft.quarterly_financials)

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show all earnings dates
msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
print(opt)
# data available via: opt.calls, opt.puts
