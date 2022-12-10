
import requests
import json
import pandas as pd
import logging as log



class ScrapCroma:
    def __init__(self):
        log.warning('<-----------------ScrapCroma Object Created ------------------->')
        #self.product = product
        pass


    def __str__(self) -> str:
        print("Web scrapping www.croma.com for iPhone")
        

    def get_data(self):
        log.warning('<-----------------Inside ScrapCroma get_data ------------------->')

        headers={"authority": "api.croma.com",
                "method": "GET",
                "path": "/product/allchannels/v1/search?currentPage=0&query=iphone%3Arelevance%3AZAStatusFlag%3Atrue%3AexcludeOOSFlag&fields=FULL",
                "scheme": "https",
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "origin": "https://www.croma.com",
                "referer": "https://www.croma.com/",
                "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
                }

        url = 'https://api.croma.com/product/allchannels/v1/search?currentPage={0}&query=iphone%3Arelevance%3AZAStatusFlag%3Atrue%3AexcludeOOSFlag&fields=FULL'

        ratings = []
        product = []
        price = []

        for j in range(0,4):
            resp=requests.get(url.format(j),headers=headers)
            #print(resp.status_code)
            #print(len(resp.content))
            #c= resp.content.decode('utf-8',errors='replace')
            #print(len(c))
            #content=c.replace('\u20b9','')
            #d=json.loads(content)
            d = json.loads(resp.content)


            for i in d['products']:
    
                try:
                    ratings.append(i['averageRating'])
                except KeyError: 
                    ratings.append(0)
                try:
                    product.append(i['name'])
                except KeyError:
                    product.append('0')
                try:
                    price.append(int(i['mrp']['value']))
                except:
                    price.append(0)


        df = pd.DataFrame(list(zip(product, price,ratings)),
                columns =['productList','Price','Rating'])
        
        return df