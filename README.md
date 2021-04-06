# Python-PPT-Comment
透過Python來抓取PPT網頁版留言

### 本次使用Python Jupyter Notebook 資料收集，以下簡易介紹如何安裝Jupyter Notebook

官方建議使用Anaconda Distribution來安裝，但本次安裝教學使用pip，如想要用Anaconda Distribution安裝，可以參考
[Anaconda Distribution](https://medium.com/python4u/anaconda%E4%BB%8B%E7%B4%B9%E5%8F%8A%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8-f7dae6454ab6)

# Python 3版本

- 1. 進行pip安裝之前建議先對pip進行版本升級
```terminal
pip3 install — upgrade pip
```
- 2. 再進行安裝Jupyter
```terminal
pip3 install jupyter
``` 

# Python 2版本

- 1. 進行pip安裝之前建議先對pip進行版本升級
```terminal
pip install — upgrade pip
```
- 2. 再進行安裝Jupyter
```terminal
pip install jupyter
``` 

# Jupyter Notebook啟動教學

- 1. 開啟terminal 輸入jupyter notebook
```terminal
jupyter notebook
```

![image](https://raw.githubusercontent.com//880831ian/Python-PPT-Comment/main/images/1.PNG)

- 2. 就可以看到瀏覽器跳出本地端的jupyter notebook介面

![image](https://raw.githubusercontent.com//880831ian/Python-PPT-Comment/main/images/2.PNG)

- 3. 點選右上角>New>Python版本>就可以新增一個編輯器

![image](https://raw.githubusercontent.com//880831ian/Python-PPT-Comment/main/images/3.PNG)

# PPT-Comment 程式碼介紹

![image](https://raw.githubusercontent.com//880831ian/Python-PPT-Comment/main/images/4.PNG)

```terminal
import requests
from bs4 import BeautifulSoup
``` 
- 因為Python要下載網頁上資料，需要使用到requests 模組建立適當的 HTTP 請求，BeautifulSoup (也是使用pip下載)會讀取HTML原始碼，會自動解析並產生BeautifulSoup的物件，裡面包含整個HTML的結構，就可以找自己想要的資料

```terminal
url = input("請輸入PPT網址(需複製文章內下方的文章網址):")
response = requests.get(url)
``` 
- 將網址輸入到欄位中，記得要使用文章下方所附的文章網址，requests會去抓取網站原始碼
