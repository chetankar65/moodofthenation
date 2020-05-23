from news import NewsFromBBC
import paralleldots
import os
import sqlite3
from paralleldots import sentiment
import time
import datetime


paralleldots.set_api_key(os.getenv('PARALLEL_DOTS'))
paralleldots.get_api_key()


#### put sentiment analysis function in a 1 hour interval
while True:
    def sentiment_tracker(text):
        sentiments = sentiment(text).get('sentiment')
        if (sentiments != None):
            max_sentiment = max(sentiments, key=sentiments.get)
            if (max_sentiment == 'positive'):
                return 3
            elif (max_sentiment == 'negative'):
                return 1
            else:
                return 2
        else:
            return 1

    #################
    def realtime():
        mood_arr = []
        conn = sqlite3.connect('mood_db')
        top_headlines = NewsFromBBC()
        conn.execute('DELETE FROM headlines')
        for headline in top_headlines:
            if (headline != None):
                #print(sentiment_tracker(headline))
                mood_arr.append(sentiment_tracker(headline))                
                conn.execute('INSERT INTO headlines (headline) VALUES (?)', (headline,))
        conn.commit()
        conn.close()
                                                                                        
        # count frequency and store in global variable
        mood = CountFrequency(mood_arr)
        
        connection = sqlite3.connect('mood_db')
        x = datetime.datetime.now()
        connection.execute('INSERT INTO current (mood, hour) VALUES (?,?)',(mood,x.strftime("%x"),))
        connection.commit()
        connection.close()
        return mood

    ######################
    def CountFrequency(my_list): 
        freq = {} 
        for item in my_list: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        return max(freq, key=freq.get)

    ####count frequency and write to a file every 1 hour (time.sleep(3600))
    realtime()
    time.sleep(3600)


