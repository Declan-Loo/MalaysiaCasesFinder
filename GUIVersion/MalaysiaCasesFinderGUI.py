from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkhtmlview import HTMLLabel
from datetime import date
from tkcalendar import Calendar

#Initialises the Tkinter window
window = Tk()

#Sets the title of the GUI app to be "Malaysian Cases Finder"
window.title('Malaysian Cases Finder')

window.geometry('825x650')

#Creates a label that describe what the app does, i.e. select a date and the number of COVID cases will be outputted, as well as the number of recoveries. It can be used for people to see the COVID-19 situation in Malaysia.
my_label = Label(window,text="Welcome to the COVID-19 Daily Cases Finder for Malaysia. \nPlease select a date, and the number of daily cases, daily recoveries will be shown in this app for that particular date.", font="Arial")
my_label.pack(pady=20,fill='both',expand=True)

#The URL for the COVID-19 page
url = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv'

#Reads the data from the CSV file stored in the url, using the pandas module function 'read_csv' with dates set as the index and converted to DateTime object in the DataFrame.
covid_data = pd.read_csv(url,parse_dates=['date'],index_col='date')

covid_data['cases_difference'] = covid_data['cases_new'] - covid_data['cases_recovered']

print(covid_data.index[0])
print(covid_data.index[-1])

cal = Calendar(window,selectmode='day',mindate=covid_data.index[0],maxdate=covid_data.index[-1],date_pattern='yyyy-mm-dd')
cal.pack(pady=20,fill='both',expand=True)

def grab_date():
    try:
        global covid_data
        #Initialises dictionary of months into the function - it is a local variable.
        month_dict={'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August','09':'September','10':'October','11':'November','12':'December'}
        date_string = ''
        my_date = cal.get_date()
        date_string = (my_date[-2:] + ' ' +month_dict[my_date[5:7]] + ' ' + my_date[:4]) 
        if covid_data.loc[my_date]['cases_difference'] < 0: 
            my_label.config(text="On date {}, there were:\n\nDaily Cases: {}\n\nRecoveries: {}\n\nThis would mean a reduction of {} active cases today.".format(date_string,int(covid_data.loc[my_date]['cases_new']),int(covid_data.loc[my_date]['cases_recovered']),int(-covid_data.loc[my_date]['cases_difference'])))
        else:
            my_label.config(text="On date {}, there were:\n\nDaily Cases: {}\n\nRecoveries: {}\n\nThis would mean an increase of {} active cases today.".format(date_string,int(covid_data.loc[my_date]['cases_new']),int(covid_data.loc[my_date]['cases_recovered']),int(covid_data.loc[my_date]['cases_difference'])))
    except:
        my_label.config(text='Invalid date given.')
my_button = Button(window, text="Select Date",command=grab_date, font=("Arial Bold",26),bg='cyan')
my_button.pack(pady=20)

my_label = Label(window,text="", font="Arial")
my_label.pack(pady=20, fill=BOTH,expand=True)


plt.style.use('ggplot')
fig, ax = plt.subplots()

sns.set_style('darkgrid')
sns.lineplot(x='date',y='cases_new',data=covid_data,alpha=0.7)
sns.lineplot(x='date',y='cases_recovered',data=covid_data,alpha=0.7)
plt.legend(['New Cases','Recovered Cases'])
plt.xlabel('Date')
plt.ylabel('Daily Cases')
plt.xticks(rotation=90)
plt.show()

window.mainloop()
