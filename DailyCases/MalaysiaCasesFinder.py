"""
Prototype program that extracts CSV data for public MOH data on COVID-19 pandemic, and outputs it to Python terminal. [CLI-based code -> soon to be GUI] 
"""

#Imports the required libraries - datetime, csv, and urllib.request
import datetime
from datetime import time
import csv
import urllib.request

#The URL of the Raw CSV file for the COVID-19 Cases in Malaysia
url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv"

#Requests the url specified earlier
webpage = urllib.request.urlopen(url)

#Read the CSV contents into a variable called casesreader
casesreader = csv.reader(webpage.read().decode('utf-8').splitlines())

#Skips a row that contains the row headings
next(casesreader)

#CSV file attached: https://github.com/MoH-Malaysia/covid19-public/blob/main/epidemic/cases_malaysia.csv

#Gets the current time now
now = datetime.datetime.now().time()

#According to the MOH, cases data for previous day is only out at 10:00am the next day
if time(10,00) > now:
  print(f"This program will output the daily cases for a user-specified date from 2020-01-25 to {datetime.date.today()-datetime.timedelta(days=2)}")
else:
  print(f"This program will output the daily cases for a user-specified date from 2020-01-25 to {datetime.date.today()-datetime.timedelta(days=1)}")


# Prompts the user for an appropriate date. If not, output "INVALID DATE GIVEN" using try-except
try:
  datecases = input("Date? {Please give format in: year-month-day} ")
  if time(10,00) > now:
      datecases = str(datetime.date.today() - datetime.timedelta(days = 2))
  if datecases == "\n":
    print("INVALID")
except:
  print("INVALID DATE GIVEN")

#The list of months 
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

try:
  #Try to access the csv (read-only)2
  
  #Initialises a list called row
  rows = []
  highest_case = -1
  for row in casesreader:
    rows.append(row)
    if datecases in row:
      print(datecases)
      year = row[0][0:4]
      month = months[int(row[0][5:7]) - 1]
      day = row[0][8:10]
      todaydate = day + " " + month + " " + year
      daily_cases = row[1]
      print(f"\nOn date {todaydate}, there were {daily_cases} daily cases.\n")
      difference = int(row[3]) - int(row[1])
      # Check if daily cases is increase or decrease in active cases. Selection
      if difference > 0:
        print(f"Meanwhile on the same day, there are {row[3]} recoveries. \nThis would mean a reduction of {difference} active cases today. \nThere was a total of {row[4]} active cases on that day.")
        print("\n\n")
      else:
        print(f"Meanwhile on the same day, there are {row[3]} recoveries. \nThis would mean an increase of {-difference} active cases today. \nThere was a total of {row[4]} active cases on that day.")

except:
  print("INVALID DATE GIVEN")
