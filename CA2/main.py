from WebScrappingAmazon import ScrapAmazon
from WebScrappingCroma import ScrapCroma
from WebScrappingFlipkart import ScrapFlipkart
import time

#sys.stdin.reconfigure(encoding='utf-8')
#sys.stdout.reconfigure(encoding='utf-8')
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

Fp = ScrapFlipkart()
Az = ScrapAmazon()
Cr = ScrapCroma()

df1 = Fp.get_data()
df2 = Az.getData()
df3 = Cr.get_data()


print('**********************************')
print("Flipkart")
print(df1.size)
print(df1.head())
print('**********************************')
print('Amazon')
print(df2.size)
print(df2.head())
print('**********************************')
print('Croma')
print(df3.size)
#input("test:")
time.sleep(1)
print(df3.dtypes)
df3['Price'].str.replace(r'/[^ .0-9]/',' ')
print('-')
print(df3.head())