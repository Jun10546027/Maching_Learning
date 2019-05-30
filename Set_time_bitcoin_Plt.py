import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#添加自定義感應器，參考網址:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.register_matplotlib_converters.html
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#資料來源
res_max = requests.get('https://www.coingecko.com/price_charts/1/usd/max.json')
jd_max = res_max.json()

#look for index
# print(jd)
df = pd.DataFrame(jd_max['stats'])
df.columns = ['datetime','value']

#時間變數的轉換設置
def set_date(row):
    #藉由開發人員工具，發現到它會把時間變數乘1000
    #格式化時間變數
    time = (row['datetime']/1000)
    time = datetime.datetime.fromtimestamp(time)
    row['datetime'] = time
    return row

#將每一行傳進set_date進行時間變數的轉換
df = df.apply(lambda row:set_date(row), axis=1)

print(df)
df.set_index('datetime',inplace=True)

mvg30 = df['value'].rolling(window=30).mean()

plt.plot(df,label = 'Bitcoin tendency')
plt.plot(mvg30,label = 'Bitcoin mvg')
plt.legend()

plt.title("All of Bitcoin tendency / month",loc="right")
plt.ylabel('value')
plt.xlabel('time')
plt.show()