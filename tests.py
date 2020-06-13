##### make sure app is running according to expectations
#### import testing modules
import unittest
import os

from flask import Flask
import requests

from app import app

#### import modules to be tested
from data import Data
from headline import Headline

###sql stuff
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

### add ons
from datetime import date 

## database configurations
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #Postgres database URL hosted on heroku
db = scoped_session(sessionmaker(bind=engine))

#### test database
class TestDatabaseConnection(unittest.TestCase):
    def test_db_connect(self):
        connect_test = db.execute('SELECT name FROM users WHERE email = :email',{'email':'chetankar65@gmail.com'}).fetchall()[0][0]
        self.assertEqual(connect_test, 'Chetan')

    ##### tested data from data.py
    def test_mood_data(self):
        test_day = date.today()
        test_data = Data.getDays(test_day)
        self.assertTrue(1 <= test_data <= 3)
    
    def test_integer_input(self):
        non_integer = 2.31
        integer_test = db.execute('INSERT INTO current (mood, hour) VALUES (:mood, :hour)',{'mood':non_integer, 'hour':})

    #### login doesn't need detailed test cases as the app is using oauth2.

class TestWebpageEndpoints(unittest.TestCase):
    def test_headline(self):
        main_url = 'http://localhost:5000/latestnews'
        test_request = requests.get(main_url)
        self.assertTrue(test_request.status_code == 200)
    
    def test_homepage(self):
        main_url = 'http://localhost:5000/'
        test_request = requests.get(main_url)
        self.assertTrue(test_request.status_code == 200)

    def page_not_found_error():
        main_url = 'http://localhost:5000/pagenotexistent'
        test_request = requests.get(main_url)
        self.assertTrue(test_request.status_code == 404 or test_request.status_code == 200)

#### test client and get pages

if __name__ == '__main__':
    unittest.main()