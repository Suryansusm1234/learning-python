import requests
import time 
def headline(category=None):
    Param=  {'pageSize': 5  }
    
    if category!=None:
        url =f"https://newsapi.org/v2/everything?q={category}&from=2024-09-20&sortBy=publishedAt&apiKey=f29c307400b347d2a21fd429205f1f60"
    else:
        url = "https://newsapi.org/v2/top-headlines?country=us&from=2024-09-20&sortBy=publishedAt&apiKey=f29c307400b347d2a21fd429205f1f60"
    response= requests.get(url)
    if response.status_code==200:
        data = response.json()
        articles = data['articles']
        return articles
    else:
        print("Sorry We were un able to get any news at the movement")
        print(f"Error:{response.status_code}")
        return None
def displaynews(articles):
    for i,article in enumerate(articles, start=1):
        print(f"Headline {i} : {article['title']}")
        print(f"content      : {article["content"]}")
        print(f"Description  : {article['description']}")
        print(f"URL          : {article['url']}")
        print(f"Source       : {article['source']['name']}")
        print(f"Published at : {article['publishedAt']}")
        print(f"URL          : {article['url']}\n")
        time.sleep(2)
def runmain():
    print("Welcome to News For all We provide valid news according to Your Request")
    category = input("Enter the category like sports,Bollywood,Tech if not sure about category press enter ")
    articles = headline(category)
    if  articles!=None:
        displaynews(articles)
if __name__ == '__main__':
    runmain()
