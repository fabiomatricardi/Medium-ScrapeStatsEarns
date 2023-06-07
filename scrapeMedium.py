import requests
import ssl
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import datetime


ssl._create_default_https_context = ssl._create_unverified_context

#========================================================================
# PASTE HERE THE CODE FROM CHROME INSPECTION FOR STATS
#========================================================================
# html_data = """ """  #to be used for test

# Reading an entire text file in Python
# tutorial from https://datagy.io/python-read-text-file/
#--------------------------------------------------------
file_path = './stat.txt'

with open(file_path) as file:
    html_data = file.read()
file.close()

html = BeautifulSoup(html_data, 'html.parser')
#------------------Create main table-------------------------------------
table = html.find_all('table',class_ = 'sortableTable js-statsTable')
#------------------find titles and create list---------------------------
raw_titles = table[0].find_all('td', class_ = 'sortableTable-rowTitle')
num_of_titles = len(raw_titles)
#----------------Generate list of the Article Titles-----------------------
title_list = []
for i in range(0,num_of_titles):
  a_title = raw_titles[i].find_all('div', class_ = 'sortableTable-title u-maxWidth450')[0]
  title_text = a_title.find('a').text
  story_num = i+1
  story_title = f"{story_num} - {title_text}"
  #print(story_title) #for initial debugging only
  title_list.append(story_title)
#-------------------------Get the sections of the table-----------------------------
raw_box = table[0].find_all('tr', class_ = 'sortableTable-row js-statsTableRow')
#-----------------Get details of the articles---------------------------------------
raw_box = table[0].find_all('tr', class_ = 'sortableTable-row js-statsTableRow')
#Generate details data of the Articles
views_list = []
reads_list = []
ratio_list = []
fans_list = []
date_list = []
hour_list = []
date_of_stat = str(datetime.datetime.now())[:10]
hour_of_stat = str(datetime.datetime.now())[11:13]
minutes = str(datetime.datetime.now())[14:16]
for i in range(0,len(raw_box)):
  details = raw_box[i].find_all('span', class_ = 'sortableTable-value')
  views = details[1].text
  reads = details[2].text
  ratio = details[3].text
  fans = details[4].text
  views_list.append(int(views))
  reads_list.append(int(reads))
  ratio_list.append(float(ratio))
  fans_list.append(int(fans))
  date_list.append(date_of_stat)
  hour_list.append(hour_of_stat)
#--------------Generate Dictionary for statistics-------------------------
Statistics = {
    "title" : title_list,
    "views" : views_list,
    "reads" : reads_list,
    "ratio" : ratio_list,
    "fans" : fans_list,
    "date" : date_list,
    "time": hour_list
}
#----------------Create and Save DataFrame-------------------------
df = pd.DataFrame(Statistics)
filename = f"Medium_Stat_{date_of_stat}at{hour_of_stat}{minutes}.csv"
df.to_csv(filename)  
print(f"File {filename} saved on your disk")
#-----Save Articles stats only related to earnings--------------------
index = [0,1,2,3,4,5,7,9,11,13,16] #order from index of the dataframe - old [0,2,4,6,10]
df_4earn = df.loc[index]
filename2 = f"Medium_4earn_{date_of_stat}at{hour_of_stat}{minutes}.csv"
df_4earn.to_csv(filename2)  
print(f"File {filename2} saved on your disk")
print("------------------------------------------------------------")

#========================================================================
# PASTE HERE THE CODE FROM CHROME INSPECTION FOR EARNINGS
#========================================================================
htmlstat = """   """ #to be used for test

# Reading an entire text file in Python
# tutorial from https://datagy.io/python-read-text-file/
#--------------------------------------------------------
file_path = './stat_earn.txt'

with open(file_path) as file:
    htmlstat = file.read()
file.close()
html2 = BeautifulSoup(htmlstat, 'html.parser')
#------------------Look for totals table-------------------------------------
totals_table = html2.find_all('div',class_ = 'u-flex u-flexRow u-xs-flexColumnReverse u-justifyContentSpaceBetween')
len(totals_table)
total_earnings = totals_table[0].find('div',class_ = 'u-inline u-fontSize22 u-uiTextThin js-payoutTotal u-fontWeightBold').text
total_referred = html2.find_all('div',class_ = 'u-inline u-fontSize22 u-uiTextThin js-payoutTotal')[1].text
total_articles = html2.find_all('div',class_ = 'u-inline u-fontSize22 u-uiTextThin js-payoutTotal')[0].text
articles_amount =total_articles[1:] 
referred_amount =total_referred[1:] 
total_amount = total_earnings[1:]
#print(total_amount)
#------------------Create main table-------------------------------------
table = html2.find_all('table',class_ = 'table u-marginTop20 u-marginBottom30 u-borderBottomLighter u-borderBottomWidth2')
stat_rows = table[0].find_all('tr', class_ = 'u-borderBottomLighter js-postPayoutRow')
tot_articles = len(stat_rows)
#-------Create deatiles stats for earning----------------------
title_earning_list = []
earn_earning_list = []
date_list = []
hour_list = []
date_of_stat = str(datetime.datetime.now())[:10]
hour_of_stat = str(datetime.datetime.now())[11:13]
minutes = str(datetime.datetime.now())[14:16]
for i in range(0,tot_articles):
  e_tit = stat_rows[i].find('a').text  #earning title
  title_earning_list.append(e_tit)
  e_earns = stat_rows[i].find('span', class_ = 'ui-body js-postAmount').text  #earning amount
  earn_earning_list.append(str(e_earns[1:]))
  date_list.append(date_of_stat)
  hour_list.append(hour_of_stat)  
#-------Create referral row------------------
title_earning_list.append("Referral Earnings")
earn_earning_list.append(referred_amount)
date_list.append(date_of_stat)
hour_list.append(hour_of_stat)
#-------Create total articles row------------------
title_earning_list.append("Articles Earnings")
earn_earning_list.append(articles_amount)
date_list.append(date_of_stat)
hour_list.append(hour_of_stat)
#-------Create summary row------------------
title_earning_list.append("Total Earnings")
earn_earning_list.append(total_amount)
date_list.append(date_of_stat)
hour_list.append(hour_of_stat)
#------------Create Dictionary------------------
earning_stats = {
    "article title" : title_earning_list,
    "earnings" : earn_earning_list,
    "date" : date_list,
    "hour" : hour_list
}
#-------------Create dataframe and save it in csv-----------------------
df1 = pd.DataFrame(earning_stats)
filename3 = f"Medium_Earn_{date_of_stat}at{hour_of_stat}{minutes}.csv"
df1.to_csv(filename3)
print(f"File {filename3} saved on your disk")
print("-------------------------------------------------------------------")
print("EARNING ARTICLES STATS")
print("-------------------------------------------------------------------")
pprint(df_4earn)
print("")
print("")
print("-------------------------------------------------------------------")
print("EARNING ARTICLES TOTALS")
print("-------------------------------------------------------------------")
pprint(df1)
print("ALL ARTICLES")
print("-------------------------------------------------------------------")
pprint(df)















"""data = requests.get(url)
print(data.text)"""