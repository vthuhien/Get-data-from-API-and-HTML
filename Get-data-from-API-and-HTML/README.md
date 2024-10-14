## About This Data
This dataset is obtained from this website: https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data <br/>
After crawling data from web, we also seek a link API with a csv file about Covid-19 pandemic data to explore and analyze it. We find a csv [file](https://api.covidtracking.com/v1/states/daily.csv) with this original API data to use

This template provides automatically updated numbers on the COVID-19 pandemic's confirmed cases and deaths. It is used on Portal:COVID-19.

The above documentation is transcluded from Template:COVID-19 pandemic data/doc. (edit | history)
Editors can experiment in this template's sandbox (edit | diff) and testcases (edit) pages.
Add categories to the /doc subpage. Subpages of this template.

## **1.Crawl Data From HTMl**
[['Location', 'Cases', 'Deaths'], </br>
 ['World[a]', '775,730,930', '7,054,878'],</br>
 ['European Union[b]', '185,732,052', '1,262,416'],</br>
 ['United States', '103,436,829', '1,191,632'],</br>
 ['China[c]', '99,369,029', '122,280'],</br>
 ['India', '45,041,192', '533,623'],</br>
 ['France', '38,997,490', '168,091'],</br>
 ['Germany', '38,437,756', '174,979'],</br>
 ['Brazil', '37,511,921', '702,116'],</br>
 ['South Korea', '34,571,873', '35,934'],</br>
 ['Japan', '33,803,572', '74,694'],</br>
 ['Italy', '26,727,644', '197,081'],</br>
 ['United Kingdom', '24,964,791', '232,112'],</br>
 ['Russia', '24,254,803', '403,155'],</br>
 ['Turkey', '17,004,718', '101,419'],</br>
 ['Spain', '13,980,340', '121,852'],</br>
 ['Australia', '11,861,161', '25,236'],</br>
 ['Vietnam', '11,624,000', '43,206'],</br>
  ...</br>
 ['Vatican City', '26', '0'],</br>
 ['Pitcairn Islands', '4', '—'],</br>
 ['North Korea', '1', '6'],</br>
 ['Turkmenistan', '0', '0'],</br>
 ["^ Countries which do not report data for a column are not included in that column's world total.\n\n^ Data on member states of the European Union are individually listed, but are also summed here for convenience. They are not double-counted in world totals.\n\n^ Does not include special administrative regions (Hong Kong and Macau) or Taiwan."]]
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...

## **2.Get Data From API**
### 1. After we crawl data from web html, we seek a link API with a csv file about Covid-19 pandemic data to explore and analyze it. We find https://api.covidtracking.com/v1/states/daily.csv this original API data to use
#### The number of positive cases and death cases statistic over time
![image](https://github.com/user-attachments/assets/dfed0b9d-de3f-4025-99ce-bc4afd34fc67)

We visualize two type of cases by one year from March 2020 to March 2021. This period is when the Corona virus begins to cause disease. As shown, we can see the number of people who have tested positive for the disease are higher over time. But, by government directives together preventation and treatment system of the medical team, this reduces the total of death cases.

As we see, although the number of positive case more and more rising, the death tolls are very low and just a fraction of positive case. This indicates that the effort of doctors and nurses and good sense of prevention disease of residents, along with the investment and support policies from government to control and decrease disease.

### 2. Assignment : get data from api by the condition of a column

- Obtain CA data of state column in month 5/2020 in native API just collected above : https://api.covidtracking.com/v1/states/daily.csv.  

- After that, transfer data to a csv file by this format API: https://api.covidtracking.com/v1/states/ca/20200501.csv </br>

![image](https://github.com/user-attachments/assets/7cc4acbc-327c-4772-a675-744b367d1bcf)
