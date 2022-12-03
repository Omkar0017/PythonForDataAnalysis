from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

class ScrapAmazon:

    def __init__(self) -> None:
        
        pass

    def __str__(self) -> str:
        print("Web scrapping www.Amazon.com for iPhone")
        pass

    def __removeBrac(self,s):
        val = s.split('>')[1].split('<')[0]
        return val

    def __removeTag(self,str):
        return str.split('>')[1].split('<')[0]
    
    def getData(self):
        priceList=[]
        productList=[]
        ratingLst=[]

        myUrl = 'https://www.amazon.in/s?k=iphone&page=2&crid=OY7745GRPJ3S&qid=1669162440&sprefix=iphone%2Caps%2C90&ref=sr_pg_{0}'

        for i in range(1,5):
            uClient = uReq(myUrl.format(i))
            page_html = uClient.read()
            uClient.close()

            pageSoup = soup(page_html,'lxml')
            products = pageSoup.findAll("span",{"class":"a-size-medium a-color-base a-text-normal"})
            price = pageSoup.findAll("span",{"class":"a-price-whole"})
            rating = pageSoup.findAll("span",{"class":"a-icon-alt"})

            for i in products:
                val = self.__removeBrac(str(i))
                productList.append(val)

            for i in price:
                val = self.__removeBrac(str(i))
                priceList.append(int(val.replace(',', '')))

            for i in rating:
                val = self.__removeBrac(str(i))
                ratingLst.append(val)


        df = pd.DataFrame(list(zip(productList, priceList,ratingLst)),
               columns =['productList','Price','Rating'])


        return df

