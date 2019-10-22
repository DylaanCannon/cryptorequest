from bs4 import BeautifulSoup
import requests

def getCryptoTable():
    url = requests.get('https://www.coinbase.com/price').text
    soup = BeautifulSoup(url, "lxml")
    #tables = soup.find_all('table')
    myTable = soup.find('table',{'class':"AssetTable__Table-sc-3hlimn-1 bgiqUG"})
    return myTable

def getCryptoPriceList():
    myTable = getCryptoTable()
    divs = myTable.find_all('div',{'class':"Flex-sc-12n1bmd-0 eDtDZD"})
    priceList = list(divs)
    finalPriceList = []
    tempMemoryVar = ""
    for price in priceList:
        price = str(price)
        tempMemoryVar = price.replace('<div class="Flex-sc-12n1bmd-0 eDtDZD"><h4 class="Header__StyledHeader-sc-1q6y56a-0 hZxUBM TextElement__Spacer-sc-18l8wi5-0 hpeTzd">','')
        tempMemoryVar = tempMemoryVar.replace('</h4></div>','')
        finalPriceList.append(tempMemoryVar)
    return finalPriceList
def getCryptoCurrencies():
    myTable = getCryptoTable()
    divs = myTable.find_all('div',{'class':"Flex-sc-12n1bmd-0 bwzQDA"})
    cryptoList = list(divs)
    finalCrpytoList = []
    tempMemoryVar = ""
    for currency in cryptoList:
        currency = str(currency)
        tempMemoryVar = currency.replace('<div class="Flex-sc-12n1bmd-0 bwzQDA"><span class="AssetTableRow__BrandedTitle-sc-1e35vph-10 buckTe"><h4 class="Header__StyledHeader-sc-1q6y56a-0 hZxUBM TextElement__Spacer-sc-18l8wi5-0 hpeTzd">','')
        tempMemoryVar = tempMemoryVar.replace('</h4></span><h4 class="Header__StyledHeader-sc-1q6y56a-0 fJEbwK TextElement__Spacer-sc-18l8wi5-0 hpeTzd">','')
        tempMemoryVar = tempMemoryVar.replace('</h4></div>','')
        finalCrpytoList.append(tempMemoryVar)
    return finalCrpytoList
    
def pairCryptoWithPrice():
    cryptoWithPrices = []
    cryptoCurrencies = getCryptoCurrencies()
    cryptoPrices = getCryptoPriceList()
    index = 0
    while index < 30:
        cryptoWithPrices.append(cryptoCurrencies[index])
        cryptoWithPrices.append(cryptoPrices[index])
        index += 1
    print(cryptoWithPrices)
pairCryptoWithPrice()









