# -*- coding: utf-8 -*-
"""Pandemic_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/vthuhien/Get-data-from-API-HTML/blob/main/Pandemic_data.ipynb

# **1.Crawl Data From HTMl**
"""

!pip install beautifulsoup4

import pandas as pd
from bs4 import BeautifulSoup as bs
import csv
import requests
import plotly.express as px
import plotly.graph_objects as go

url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data'
res = requests.get(url)
text_data = bs(res.text, "html.parser")

get_data = text_data.findAll("table" , {"class":"wikitable"})[0]
rows = get_data.findAll("tr")
data = []
for i2 in rows:
  cell = [i.get_text().strip() for i in i2.findAll(["td", "th"]) if len(i.get_text().strip())>0]
  data.append(cell)
print(len(data))
data

df = pd.DataFrame(data[1:], columns = data[0])
df

"""# **2.Get Data From API**
#### 1.After we crawl data from web html, we seek a link API with a csv file about Covid-19 pandemic data to explore and analyze it. We find https://api.covidtracking.com/v1/states/daily.csv this original API data to use
"""

url = "https://api.covidtracking.com/v1/states/daily.csv"
data = pd.read_csv(url)
pd.set_option('display.max_columns',500)
data

"""To clean this data, we will filter the values that can't be converted to date time values and change them into null value as Nan"""

data['lastUpdateEt'] = pd.to_datetime(data['lastUpdateEt'])
data['date'] = data['date'].apply(lambda x: pd.to_datetime(x, format = '%Y%m%d', errors ='coerce'))

# data['checkTimeEt'] = [ str(i) + '2021' for i in data['checkTimeEt']]

rs= []
for i in data['checkTimeEt']:
  if pd.notna(i):
    a = i[0:5]
    b = i[5:]
    rs.append(f'{a}/2021{b}')
df = pd.Series(rs)

# print(df[df.apply(lambda x: pd.to_datetime(x, format='%m/%d/%Y %H:%M', errors ='coerce') is pd.NaT)])
df = df.replace('02/29/2021 22:00' , '02/28/2021 22:00')
df = df.replace('02/29/2021 19:00' , '02/28/2021 19:00')

df2 = pd.to_datetime(df)
df_date_time = pd.DataFrame( {'time':df2})
data['checkTimeEt'] = df_date_time['time']
data

"""#### The number of positive cases and death cases statistic over time"""

# data['positive','death'] = data['positive','death'].replace()

null_value = data[data['positive'].isnull()]
# total_null_value = data['positive'].isnull().sum()

data[['positive','death']] = data[['positive','death']].fillna(0, inplace =False)
cases = data.groupby(['date']).agg(positive_case = ('positive', 'sum'),
                    death_case = ('death', 'sum')).reset_index()

cases.sort_values( by = 'positive_case', ascending = False, inplace = True)
cases

fig = go.Figure( data = [
     go.Bar( x = cases['date'].values, y = cases['positive_case'].values, name = 'Position Case'),
    go.Bar(x = cases['date'].values, y = cases['death_case'].values, name = 'Death Cases')]
)
fig.update_layout(
    xaxis_title = 'date time',
    yaxis_title = 'values',
    title = 'Compare Postive Cases vs Death Cases',
    font = dict( size = 17, family = "Franklin Gothic")

)
fig.show()

"""We visualize two type of cases by one year from March 2020 to March 2021. This period is when the Corona virus begins to cause disease. As shown, we can see the number of people who have tested positive for the disease are higher over time. But, by government directives together preventation and treatment system of the medical team, this reduces the total of death cases.


As we see, although the number of positive case more and more rising, the death tolls are very low and just a fraction of positive case. This indicates that the effort of doctors and nurses and good sense of prevention disease of residents, along with the investment and support policies from government to control and decrease disease.

### 2. Assignment : get data from api by the condition of a column

- Obtain CA data of state column in month 5/2020 in native API just collected above : https://api.covidtracking.com/v1/states/daily.csv.  

- After that, transfer data to a csv file by this format API: https://api.covidtracking.com/v1/states/ca/20200501.csv
"""

url = 'https://api.covidtracking.com/v1/states/daily.csv'
total_data = pd.read_csv(url)
pd.set_option('display.max_columns',500)
total_data

"""- We realized that there was a need to apply each day value in the API in this format : https://api.covidtracking.com/v1/states/{state}/{YYYYmmdd}.csv
- So we must create a list of all date time on May of 2020 <br>
- Then, with each date time value, we will call back API once time
"""

from datetime import date, timedelta
def generate_date(start_day, end_day):
  date_modified = start_day
  all_date = [start_day]
  while date_modified < end_day:
    date_modified += timedelta( days = 1)
    all_date.append(date_modified)
  return all_date
sday = date(2020,5,1)
eday = date(2020,5,31)
dates = generate_date(sday, eday)
# print(dates[0:3])
for d in dates:
  print(d)

def get_data_by_date( dates, state):
  all_date = dates.strftime('%Y%m%d')
  format_url = f"https://api.covidtracking.com/v1/states/{state}/{all_date}.csv"
  # print(format_url)
  data = pd.read_csv(format_url)
  return data

for date in dates:
    get_data_by_date(date, 'ca')

from time import sleep
df = pd.DataFrame()
for date in dates:
  data = get_data_by_date(date,'ca')
  df =pd.concat([df, data],ignore_index = True)
  sleep(1)