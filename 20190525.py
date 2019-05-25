import requests
from bs4 import BeautifulSoup

url = "https://tw.appledaily.com/new/realtime"

respond = requests.get(url)

soup = BeautifulSoup(respond.text,'lxml')
for news in soup.select('.rtddd a'):
    print(news.select_one("h1"))
    # if news.select_one("h1"):
    #     h1 = news.select("h1")[0].text
    #     h2 = news.select("h2")[0].text
    #     time = news.select("time")[0].text
    #     print(h1,h2,time)