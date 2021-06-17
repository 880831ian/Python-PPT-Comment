#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
from bs4 import BeautifulSoup

#所要擷取的網站網址

#url = 'https://www.ptt.cc/bbs/Bank_Service/M.1613981823.A.106.html'
url = input("請輸入PPT網址(需複製文章內下方的文章網址):")
#建立回應
response = requests.get(url)
#印出網站原始碼
#print(response.text)

#將原始碼做整理
soup = BeautifulSoup(response.text, 'lxml')
#使用find_all()找尋特定目標
articles = soup.find_all('div', 'push')
#print(articles)
#寫入檔案中
with open('message.txt','a+') as f:
    for article in articles:
        #去除掉冒號和左右的空白
        messages = article.find('span','f3 push-content').getText().replace(':','').strip()
        print(messages)
        f.write(messages + "\n")

