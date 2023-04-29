# this program will pull stock information and data and display a simple visualization of historic data
# written by Joshua Shiman

# CODING BEGINS HERE

# dictionary
# perchange is percent change from yesterday's close to today's current price

# imports
import yfinance as yf
from sty import fg, bg, ef, rs
import pandas as pd
from datetime import date, timedelta
import matplotlib.pyplot as plt


# stock selection and defining
print("Please enter a stock ticker:")
tickerSymbol = input()
tickerData = yf.Ticker(tickerSymbol)
dict = tickerData.info

# display front end information
print("\n")
print(dict["longName"])
print(dict["sector"])
print(dict["industry"])
print("\n")

# defining variables
currency = dict["financialCurrency"]
currprice = (dict["currentPrice"])
prevprice = (dict["previousClose"])
revenue = (dict["totalRevenue"])
debt = (dict["totalDebt"])
premrkt = (dict["preMarketPrice"])
pe = (dict["forwardPE"])
divrate = (dict["dividendRate"])
mrktcap = (dict["marketCap"])
vol = (dict["volume"])

# formulas
daychnge = currprice-prevprice
perchnge = (daychnge/currprice)*100

# printing information
if daychnge > 0:
    color = fg.green + "$ " + str("{:.2f}".format(daychnge)) + " or " + "{:.1f}".format(perchnge) + "%" + fg.rs
    print(color)
elif daychnge <= 0:
    color = fg.red + "$ " + str("{:.2f}".format(daychnge)) + " or " + "{:.1f}".format(perchnge) + "%" + fg.rs
    print(color)

print("Yesterday Close", "= ", currency, prevprice)
print("Current Price", "= ", currency, end="")
if currprice > prevprice:
    color = fg.green + str(currprice) + fg.rs
    print(" ", color)
elif currprice <= prevprice:
    color = fg.red + str(currprice) + fg.rs
    print(" ", color)

# printing fundamentals
print("\n")
print("Dividend Rate =", divrate)
print("P/E =", end="")
if pe > 15:
    color = fg.red + str("{:.2f}".format(pe)) + fg.rs
    print(" ", color)
elif pe <= 15:
    color = fg.green + str("{:.2f}".format(pe)) + fg.rs
    print(" ", color)

# printing trading data
print("\n")
print("Market Cap =", mrktcap)
print("Volume =", vol)

# printing financials
print("\n")
print("Revenue =", revenue)
print("Debt =", debt)

# earnings calendar
print(tickerData.calendar)

# stock graph
Start = date.today() - timedelta(365)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')

def closing_price(tickerSymbol):
    Asset = pd.DataFrame(yf.download(tickerSymbol, start=Start,
      end=End)['Adj Close'])
    return Asset


# plotting
graph = closing_price(tickerSymbol)
plt.plot(graph, color='green', linewidth=2)
plt.title(str(dict["longName"]) + str(" Performance"))
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.show()
plt.show()


