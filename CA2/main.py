from WebScrappingAmazon import ScrapAmazon
from WebScrappingCroma import ScrapCroma
from WebScrappingFlipkart import ScrapFlipkart
import time



Fp = ScrapFlipkart()
Az = ScrapAmazon()
Cr = ScrapCroma()

df1 = Fp.get_data()
df2 = Az.getData()
df3 = Cr.get_data()


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
#print(df3.info())
#s = int(input("Please Select Which iPhone you would like to select \n 1: iPhone 12 \n 2: iPhone 13 \n 3: iPhone 14"))
s = 2
if s == 1:
    name = 'Apple\iPhone\12'
elif s ==2:
    name = 'Apple\iPhone\13'
elif s == 3:
    name = 'Apple\iPhone\14'
else:
    print("Invalid input")

print(df1.info())   
fkDf = df1.query('productList.str.contains({0})'.format(name))
print(fkDf.head())