#### Graph logic here
import psycopg2
import datetime
import csv
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = process.env.DATABASE_URL

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))

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
    for row in db.execute('SELECT * FROM current WHERE hour = :date',{"date":today.strftime("%x")}):
        today_arr.append(row[1])
    for row in db.execute('SELECT * FROM current WHERE hour = :date',{"date":yesterday.strftime("%x")}):
        yesterday_arr.append(row[1])
    for row in db.execute('SELECT * FROM current WHERE hour = :date',{"date":daybeforeyesterday.strftime("%x")}):
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

