import requests
import os
      
  
def NewsFromBBC(): 
      
    # BBC news api 
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&country=in&category=business&sortBy=top&apiKey={key}".format(key = os.getenv("NEWSAPI"))
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
    for ar in article: 
        results.append(ar["description"]) 
        
    return results                  
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  

