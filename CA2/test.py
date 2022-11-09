import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


from bs4 import BeautifulSoup as bs

f = 'D:\HTML_STUDY\sololearn.html'

with open(f,'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = bs(content,'lxml')
    #print(soup.prettify())
    tags = soup.find_all('h1')
    #for i in tags:
        #print(i.text)


    sections = soup.find_all('div',class_ = 'section')
    for i in sections:
        print(i.h1)
        #print(i.h1.text)

