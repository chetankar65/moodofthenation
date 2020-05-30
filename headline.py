#from db import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

DATABASE_URL = process.env.DATABASE_URL

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
    
