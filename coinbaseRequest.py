from bs4 import BeautifulSoup
import requests

#useful function for other programs, returns the main table for coinbase.com/price. This can be modified quickly for any webpage
def getCryptoTable():
    url = requests.get('https://www.coinbase.com/price').text
    soup = BeautifulSoup(url, "lxml")
    myTable = soup.find('table',{'class':"AssetTable__Table-sc-3hlimn-1 bgiqUG"})
    return myTable

def getCryptoPriceList():
    myTable = getCryptoTable()
    divs = myTable.find_all('div',{'class':"Flex-sc-12n1bmd-0 eDtDZD"})
    priceList = list(divs)
    finalPriceList = []
    tempMemoryVar = ""
    #this for loop iterates through each item in the price list end replaces all content besides the price with an empty string and 
    #the appends the new string into the final price list
    for price in priceList:
        price = str(price)
        #'string'.replace is used many times through out this program, it finds a substring within a string and replaces it with any content 
        # of your choice
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

#The convertPricesToFloat() function does as its name says, by removing the dollar sign and commas from the crypto prices gathered in getCryptoPriceList()
#it then converts each item to float and appends them to floatPriceList and returns that value
def convertPricesToFloat():
    priceList = getCryptoPriceList()
    tempMemoryVar = 0.0
    newPriceList = []
    floatPriceList = []
    for price in priceList:
        price = str(price)
        tempMemoryVar = price.replace('$','')
        tempMemoryVar = tempMemoryVar.replace(',','')
        newPriceList.append(tempMemoryVar)
    for price in newPriceList:
        price = float(price)
        floatPriceList.append(price)
    return floatPriceList
        
#pairCryptoWithPrice() is a usefull function for visualizing the data coinBaseRequest.py retrieves from coinbase.com/price
def pairCryptoWithPrice():
    cryptoWithPrices = []
    cryptoCurrencies = getCryptoCurrencies()
    cryptoPrices = convertPricesToFloat()
    index = 0
    while index < 30:
        cryptoWithPrices.append(cryptoCurrencies[index])
        cryptoWithPrices.append(cryptoPrices[index])
        index += 1
    print(cryptoWithPrices)
pairCryptoWithPrice()








