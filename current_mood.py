from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

DATABASE_URL = 'postgresql+psycopg2://ljcnuxagkumbwa:acdb25f7e24cc31d92dd48347a675e59e7740dd51b0b09bcf87b3162c6222e0c@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d89hhd9gpdpvfm'

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
        current = db.execute('SELECT mood FROM current ORDER BY id DESC LIMIT 3').fetchall()
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
    
