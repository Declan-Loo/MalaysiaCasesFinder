import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#The URL for the COVID-19 page
url = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv'

#Reads the data from the CSV file stored in the url, using the pandas module function 'read_csv' with dates set as the index and converted to DateTime object in the DataFrame.
covid_data = pd.read_csv(url,parse_dates=['date'],index_col='date')

covid_data['cases_difference'] = covid_data['cases_new'] - covid_data['cases_recovered']

print(covid_data.index[0])
print(covid_data.index[-1])

datecases = input("Date? {Please give format in: year-month-day} ")

print("On date {}, there were {} daily cases.".format(datecases,int(covid_data.loc[datecases]['cases_new'])))

if covid_data.loc[datecases]['cases_difference'] < 0:
    print("Meanwhile on the same day, there are {} recoveries. This would mean a reduction of {} active cases today.".format(int(covid_data.loc[datecases]['cases_recovered']),int(-covid_data.loc[datecases]['cases_difference'])))
else:
    print("Meanwhile on the same day, there are {} recoveries. This would mean an increase of {} active cases today.".format(int(covid_data.loc[datecases]['cases_recovered']),int(covid_data.loc[datecases]['cases_difference'])))


#Creates a Matplotlib graph
plt.style.use('ggplot')

#Creates a subplot
fig, ax = plt.subplots()

#Sets the style to the darkgrid style of Seaborn
sns.set_style('darkgrid')
#Creates a lineplot with the date as the x-axis and cases_new as the y-axis, with data from covid_data DataFrame, and the opacity being 0.7 (betwwen 0 and 1) in the subplot
sns.lineplot(x='date',y='cases_new',data=covid_data,alpha=0.7)
#Creates a lineplot with the date as the x-axis and cases_recovered as the y-axis, with data from covid_data DataFrame, and the opacity being 0.7 (betwwen 0 and 1) in the same subplot
sns.lineplot(x='date',y='cases_recovered',data=covid_data,alpha=0.7)
#Creates new legends of 'New Cases' and 'Recovered Cases'
plt.legend(['New Cases','Recovered Cases'])
#Names the X-Label 'Date'
plt.xlabel('Date')
#Names the Y-Label 'Daily Cases'
plt.ylabel('Daily Cases')

#Rotates the xticks 90 degrees clockwise
plt.xticks(rotation=90)

#Shows the subplot
plt.show()

#Saves the graph into an image
plt.savefig('NewVSRecovered.png')

#Clears the plot afterwards
plt.clf()
