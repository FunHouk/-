import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib

import matplotlib.pyplot as plt 
from IPython.display import display
plt.style.use('fivethirtyeight')
sns.set_style('ticks',{'font.sans-serif':['simhei','Arial']})

battery_df = pd.read_csv('learn/battery_U.csv')
#display(battery_df.head(n=2))
#battery_df.info()
#print (battery_df.describe())
columns = ['0.1M','0.2M','0.4M','0.8M']
df = battery_df.copy()
df1 = battery_df.copy()
df1['temp'] = df1.loc[(df1['temp'] < 90 ),'temp'] 

sns.set_style('dark')

fig,[ax1,ax2] = plt.subplots(2,1)

plt.subplot(211)
for i,item in enumerate(columns):
    sns.lineplot(df['temp'],df[item],label=item,lw=1.5)
plt.locator_params('y',nbins = 10)
plt.ylabel('70-100 C capicity')

plt.subplot(212)
for i,item in enumerate(columns):
    sns.lineplot(df1['temp'],df1[item],label=item,lw=1.5)
plt.locator_params('y',nbins = 10)
plt.ylabel('70-90 C capicity')



plt.legend()
plt.show()



