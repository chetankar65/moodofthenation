import requests      
  
def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=cf454be3d2784854a6d0c0e3b6363c29"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["description"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i])                  
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  

