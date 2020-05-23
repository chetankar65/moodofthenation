from selenium import webdriver
import unittest
import os
import sqlite3
from db import init_db_command
from news import NewsFromBBC
from user import User

# Naive database setup; Database testing

try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

NewsFromBBC()

######### Selenium testing for frontend
def selenium_testing():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
    #options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(chrome_options=options,executable_path='https://localhost:5000')
    driver.get()

    python_button = driver.find_element_by_id("login")
    python_button.click()

#####Sentiment analysis tests
#print(sentiment('Outage monitor records thousands of reports of issues'))
