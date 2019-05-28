import requests
import pandas
import matplotlib.pyplot as plt

#資料來源
res_max = requests.get('https://www.coingecko.com/price_charts/1/usd/max.json')
jd_max = res_max.json()

res_year = requests.get('https://www.coingecko.com/price_charts/1/usd/custom.json?from=1527379200&to=1558828800')
jd_year = res_year.json()

#look for index
# print(jd)
df = pandas.DataFrame(jd_max['stats'])
df.columns = ['datetime','value']

#set_index => 參考:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
# (inplace : bool, default False )        Modify the DataFrame in place (do not create a new object).
#設定index
df.set_index('datetime',inplace=True)
# print(df)

#繪製移動平均線
df['mvg30'] = df['value'].rolling(window=30).mean()

#設定位置
plt.subplot(2,1,1)
plt.plot(df)

#設定title，y軸，X軸
plt.title("All of Bitcoin tendency / month",loc="right")
plt.ylabel('value')
plt.xlabel('time')

#設定位置
df1 = pandas.DataFrame(jd_year['stats'])
df1.columns = ['datetime','value']

#設定index
df1.set_index('datetime',inplace=True)

#設定移動平均線
df1['mvg7'] = df1['value'].rolling(window=7).mean()

#定位，畫出來
plt.subplot(3,1,3)
plt.plot(df1)

#設定 title , 設定x軸，Y軸
plt.title("Bitcoin tendency of year / week",loc="right")
plt.xlabel('time')
plt.ylabel('value')
plt.show()

