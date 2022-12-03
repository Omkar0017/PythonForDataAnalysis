from WebScrappingAmazon import ScrapAmazon
from WebScrappingCroma import ScrapCroma
from WebScrappingFlipkart import ScrapFlipkart
import pandas as pd
import matplotlib.pyplot as plt



Fp = ScrapFlipkart()
Az = ScrapAmazon()
Cr = ScrapCroma()
template = "An exception of type {0} occurred."

df1 = pd.DataFrame()

"""
df2 = pd.DataFrame()
df3 = pd.DataFrame()


try:
    df1 = Fp.get_data()
except  Exception as ex :
    print(template.format(type(ex).__name__))
    
try:  
    df2 = Az.getData()
except  Exception as ex :
    print(template.format(type(ex).__name__))

try:
    df3 = Cr.get_data()
except  Exception as ex :
    print(template.format(type(ex).__name__))


print('**********************************')
print("Flipkart")
print(df1.size)
#print(df1.head())
#print(df1.info())
print('**********************************')
print('Amazon')
print(df2.size)
#print(df2.head())
#print(df2.info())

print('**********************************')
print('Croma')

print(df3.size)
#print(df3.head())
print(df1.info())
s = int(input("Please Select Which iPhone you would like to select \n 1: iPhone 12 \n 2: iPhone 13 \n 3: iPhone 14"))
s = 2
if s == 1:
    name = 'Apple\iPhone\12'
elif s ==2:
    #name = 'Apple\tiPhone\t13'
    name = '13'
elif s == 3:
    name = 'Apple\iPhone\14'
else:
    print("Invalid input")

print(df1.info())   
print('productList.str.contains({0})'.format(name))
fkDf = df1.query('productList.str.contains({0})'.format(name))
print(fkDf.head())"""




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

