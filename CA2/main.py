from WebScrappingAmazon import ScrapAmazon
from WebScrappingCroma import ScrapCroma
from WebScrappingFlipkart import ScrapFlipkart
import pandas as pd
import matplotlib.pyplot as plt
import logging as log




Fp = ScrapFlipkart()
Az = ScrapAmazon()
Cr = ScrapCroma()
template = "An exception of type {0} occurred."

df1 = pd.DataFrame()


status = 'Y'
while status == 'Y':
    print("Please Select Which Website you would like to select \n 1 for Flipkart.com  \n 2 for Amazon.in  \n 3 for Croma.com")
    site = int(input("Input: "))

    if site == 1:
        name = 'Flipkart'
        try:
            df1 = Fp.get_data()
            finalDf = df1.sort_values('Price',ascending= True).head(20)

            plt.figure(figsize=(10,10))
            plt.barh(finalDf['productList'],finalDf['Price'])
            plt.xlabel('Name')
            plt.ylabel('Price')
            plt.grid()
            plt.title('Price vs Product for Flipkart')
            plt.show()

        except  Exception as ex :
            print(template.format(type(ex).__name__))


    elif site == 2:
        name = 'Amazon'
        try:
            df1 = Az.getData()
            finalDf = df1.sort_values('Price',ascending= True).head(20)

            plt.figure(figsize=(10,10))
            plt.barh(finalDf['productList'],finalDf['Price'])
            plt.xlabel('Name')
            plt.ylabel('Price')
            plt.grid()
            plt.title('Price vs Product for Amazon')
            plt.show()
        except  Exception as ex :
            print(template.format(type(ex).__name__))

    elif site == 3:
        name = 'Croma'
        try:
            df1 = Cr.get_data()
            finalDf = df1.sort_values('Price',ascending= True).head(20)
     
            plt.figure(figsize=(10,10))
            plt.barh(finalDf['productList'],finalDf['Price'])
            plt.xlabel('Name')
            plt.ylabel('Price')
            plt.grid()
            plt.title('Price vs Product for Croma')
            plt.show()
        except  Exception as ex :
            print(template.format(type(ex).__name__))
        
        
    else:
        print("Invalid input")
        

    status = input('Do you want to try Again  Y/N ?').capitalize()
    print(status)

