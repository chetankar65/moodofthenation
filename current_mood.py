from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))

class Current():
    def __init__(self,mood):
        self.mood = mood

    #This means you can put a function inside a class 
    #but you can't access the instance of that class 
    #(this is useful when your method does not use the instance).
    @staticmethod
    def get():
        current = db.execute('SELECT mood FROM current ORDER BY id DESC LIMIT 4').fetchall()
        return current
    
    @staticmethod
    def create(mood,hour):
        db.execute(
            "INSERT INTO current (mood, hour) "
            "VALUES (?,?)",
            (mood,hour),
        )
        db.commit()
    
    @staticmethod
    def delete():
        db.execute("DELETE FROM current")
        db.commit()
    
