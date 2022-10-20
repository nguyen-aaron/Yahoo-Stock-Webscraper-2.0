from bs4 import BeautifulSoup
import requests
import time

def dailyStocks():
  startTime = time.time()
  listLength = 5
  def getTrendingStocks():
    page = requests.get("https://finance.yahoo.com/trending-tickers")
    soup = BeautifulSoup(page.content, "html.parser")
    stockNameList = soup.find_all(attrs = {"aria-label" : "Name"})[0:listLength]
    stockPriceList = soup.find_all(attrs = {"aria-label" : "Last Price"})[0:listLength]
    stockChangeList = soup.find_all(attrs = {"aria-label" : "% Change"})[0:listLength]
    print("Today's Trending:")
    for x in range(0, listLength):
      print(stockNameList[x].text, "-->", stockPriceList[x].text, "-->", stockChangeList[x].text)
    print("")

  def getGainers():
    page = requests.get("https://finance.yahoo.com/gainers")
    soup = BeautifulSoup(page.content, "html.parser")
    stockNameList = soup.find_all(attrs = {"aria-label" : "Name"})[0:listLength]
    stockPriceList = soup.find_all(attrs = {"aria-label" : "Price (Intraday)"})[0:listLength]
    stockChangeList = soup.find_all(attrs = {"aria-label" : "% Change"})[0:listLength]
    print("Today's Winners:")
    for x in range(0, listLength):
      print(stockNameList[x].text, "-->", stockPriceList[x].text, "-->", stockChangeList[x].text)
    print("")

  def getLosers():
    page = requests.get("https://finance.yahoo.com/losers")
    soup = BeautifulSoup(page.content, "html.parser")
    stockNameList = soup.find_all(attrs = {"aria-label" : "Name"})[0:listLength]
    stockPriceList = soup.find_all(attrs = {"aria-label" : "Price (Intraday)"})[0:listLength]
    stockChangeList = soup.find_all(attrs = {"aria-label" : "% Change"})[0:listLength]
    print("Today's Losers:")
    for x in range(0, listLength):
      print(stockNameList[x].text, "-->", stockPriceList[x].text, "-->", stockChangeList[x].text)
    print("")

  def getETFs():
    page = requests.get("https://finance.yahoo.com/etfs")
    soup = BeautifulSoup(page.content, "html.parser")
    stockNameList = soup.find_all(attrs = {"aria-label" : "Name"})[0:listLength]
    stockPriceList = soup.find_all(attrs = {"aria-label" : "Price (Intraday)"})[0:listLength]
    stockChangeList = soup.find_all(attrs = {"aria-label" : "% Change"})[0:listLength]
    print("Today's Top ETFs:")
    for x in range(0, listLength):
      print(stockNameList[x].text, "-->", stockPriceList[x].text, "-->", stockChangeList[x].text)
    print("")
  
  def getWorldIndices():
    page = requests.get("https://finance.yahoo.com/world-indices")
    soup = BeautifulSoup(page.content, "html.parser")
    stockNameList = soup.find_all(attrs = {"aria-label" : "Name"})[0:listLength]
    stockPriceList = soup.find_all(attrs = {"aria-label" : "Last Price"})[0:listLength]
    stockChangeList = soup.find_all(attrs = {"aria-label" : "% Change"})[0:listLength]
    print("Today's World Indices:")
    for x in range(0, listLength):
      print(stockNameList[x].text, "-->", stockPriceList[x].text, "-->", stockChangeList[x].text)
    print("")
  getTrendingStocks()
  getGainers()
  getLosers()
  getETFs()
  getWorldIndices()
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("The elsapsed time is", elapsedTime, "seconds.")

dailyStocks()