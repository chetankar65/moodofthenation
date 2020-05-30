#from db import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

DATABASE_URL = 'postgresql+psycopg2://ljcnuxagkumbwa:acdb25f7e24cc31d92dd48347a675e59e7740dd51b0b09bcf87b3162c6222e0c@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d89hhd9gpdpvfm'

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))

class Headline():
    def __init__(self, headline):
        self.headline = headline

    #This means you can put a function inside a class 
    #but you can't access the instance of that class (this is useful when your method does not use the instance).
    @staticmethod
    def get():
        headlines = db.execute("SELECT * FROM headlines").fetchall()            
        return headlines

    @staticmethod
    def create(headline):
        db.execute("INSERT INTO headlines (headline) VALUES (:headline)",{"headline":headline})
        db.commit()
    
    @staticmethod
    def delete():
        db.execute("DELETE FROM headlines")
        db.commit()
    
