# These lines of code perform 4 functions with the user panel. Use(Json type data)

# 1- It visits the api.themoviedb.org website and brings up the list of the most popular movies.

# 2- Visits the Api.themoviedb.org website and fetches movies currently on show.

# 3- Visits the api.themoviedb.org website and brings up the upcoming movies.

# 4- Visits the api.themoviedb.org website and fetches a list of movies based on the keyword the user entered.

# Used libraries : Json, Requests

import json
import requests

# popular?    
# now_playing?
# upcoming?
# walking/keywords?

class Movie():
    
        
    def __init__(self):
        
        self.api_url="https://api.themoviedb.org/3/movie/"  
        self.api_key="?api_key=4315c925748e7f3c7d09e746fe4e63d3&language=en-US&page=1"
        
        
    def getMostPopular(self):
        
        result=requests.get(self.api_url+"popular"+self.api_key).json()
        return result
        
    
    def getNowPlaying(self):
        result=requests.get(self.api_url+"now_playing"+self.api_key).json()
        return result
    
    def getUpComing(self):
        result=requests.get(self.api_url+"upcoming"+self.api_key).json()
        return result
    
   
    def SearchKey(self,keyword):
        
        result=requests.get("https://api.themoviedb.org/3/search/keyword?api_key=4315c925748e7f3c7d09e746fe4e63d3&"+"query="+keyword+"&page=1").json()
        return result
    


movie=Movie()        
while True:
    
    print("Menu".center(50,"*"))
    islem=input("1) - Most Popular Movies\n2) - Now Playing Movies\n3) - Get Upcoming Movies\n4) - Keywords-Search\n5) - Exit")
    
    if islem=="5":
        break
    else:
        
        if islem=="1":
            result=movie.getMostPopular()
            sayac=1
            for i in result["results"]:
                
                print(sayac,i["title"])
                sayac+=1
        
        elif islem=="2":
            result=movie.getNowPlaying()
            sayac=1
            
            for i in result["results"]:
                print(sayac,i["title"])
                sayac+=1
        
        elif islem=="3":
            result=movie.getUpComing()
            sayac=1
            for i in result["results"]:
                print(sayac,i["title"])
                sayac+=1
        
        elif islem=="4":
            keyword=input("Anahtar kelime: ")
            result=movie.SearchKey(keyword)
            sayac=1
            for i in result["results"]:
                print(sayac,i["name"])
                sayac+=1
        
        
        else:
            print("Yanlış tuşlama! ")
            
   
    

    
    
