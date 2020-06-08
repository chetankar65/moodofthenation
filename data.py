from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2
import os


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))

class Data():
    #### initilialise function
    def __init__(self, time):
        self.time = time

    @staticmethod
    def getDays(time):
        ### Get average of all moods for today, yesterday, day before yesterday, and a few days before that
        mood_avg = db.execute('SELECT avg(mood) FROM current WHERE hour = :hour',{"hour":time}).fetchall()
        return mood_avg
    
    @staticmethod
    def getMonths(time):
        ### write a logic to get data for months
        mood_avg = db.execute('SELECT avg(mood) FROM current WHERE hour = :hour',{"hour":time}).fetchall()
        return mood_avg
    
    @staticmethod
    def getTimeline():
        #### get 8 hour timeline
        current = db.execute('SELECT mood FROM current ORDER BY id DESC LIMIT 9').fetchall()
        return current