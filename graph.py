#### Graph logic here
import sqlite3
import datetime
import csv
import time

#datetime.date.today() + datetime.timedelta(days=1)

def CountFrequency(my_list): 
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return max(freq, key=freq.get)

while True:
    db = sqlite3.connect('mood_db')
    today = datetime.datetime.now()
    yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)
    daybeforeyesterday = datetime.datetime.now() + datetime.timedelta(days=-2)

    today_arr = []
    yesterday_arr = []
    day_before_yesterday = []
    for row in db.execute('SELECT * FROM current WHERE hour = ?',(today.strftime("%x"),)):
        today_arr.append(row[1])
    for row in db.execute('SELECT * FROM current WHERE hour = ?',(yesterday.strftime("%x"),)):
        yesterday_arr.append(row[1])
    for row in db.execute('SELECT * FROM current WHERE hour = ?',(daybeforeyesterday.strftime("%x"),)):
        day_before_yesterday.append(row[1])

    
    #############
    if(len(day_before_yesterday) == 0):
        day_before_data = 0
    else:
        day_before_data = CountFrequency(day_before_yesterday)
    
    if(len(yesterday_arr) == 0):
        yesterday_data = 0
    else:
        yesterday_data = CountFrequency(yesterday_arr)
    
    ##############
    
    if(len(today_arr) == 0):
        today_data = 0
    else:
        today_data = CountFrequency(today_arr)
    ############
    filename = "graph_data.csv"
    with open(filename, 'w') as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(csvfile) 
        if (csvreader.line_num == 2):
            csvreader.truncate()
            csvwriter.writerow([day_before_data,yesterday_data,today_data])
            csvwriter.writerow([daybeforeyesterday.strftime("%x"),yesterday.strftime("%x"),today.strftime("%x")])
        else:
            csvwriter.writerow([day_before_data,yesterday_data,today_data])
            csvwriter.writerow([daybeforeyesterday.strftime("%x"),yesterday.strftime("%x"),today.strftime("%x")])

    
    time.sleep(3600)

