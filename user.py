from flask_login import UserMixin
import psycopg2
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))
class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    #This means you can put a function inside a class 
    #but you can't access the instance of that class (this is useful when your method does not use the instance).
    @staticmethod
    def get(user_id):
        user = db.execute("SELECT * FROM users WHERE id = :id",{"id":user_id}).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        db.execute("INSERT INTO users (id, name, email, profile_pic) VALUES (:id, :name, :email, :profile)",{"id":id_, "name":name, "email":email, "profile":profile_pic})
        db.commit()
        db.close()
    
