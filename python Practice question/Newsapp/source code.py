import requests
import time 
url ="https://newsapi.org/v2/top-headlines"
headers = {
    'Authorization': 'f29c307400b347d2a21fd429205f1f60'  # Replace with your actual API key
}
def headline(contrycode = 'us',category=None):
    Param=  {'country':contrycode,'pageSize': 5  }
    if category!=None:
        Param['category']=category
    
    response= requests.get(url, headers=headers, params=Param)
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
        time.sleep(4)
def runmain():
    print("Welcome to News For all We provide valid news according to Your Request")
    country_name = input("Enter the contry ")
    country_name = country_name.title()
    category = input("Enter the category like sports,Bollywood,Tech if not sure about category press enter")
    country_codes = {
    "Argentina": "ar",
    "Austria": "at",
    "Australia": "au",
    "Belgium": "be",
    "Brazil": "br",
    "Bulgaria": "bg",
    "Canada": "ca",
    "China": "cn",
    "Colombia": "co",
    "Cuba": "cu",
    "Czech Republic": "cz",
    "Egypt": "eg",
    "France": "fr",
    "Germany": "de",
    "Greece": "gr",
    "Hong Kong": "hk",
    "Hungary": "hu",
    "India": "in",
    "Indonesia": "id",
    "Ireland": "ie",
    "Israel": "il",
    "Italy": "it",
    "Japan": "jp",
    "Latvia": "lv",
    "Lithuania": "lt",
    "Malaysia": "my",
    "Mexico": "mx",
    "Morocco": "ma",
    "Netherlands": "nl",
    "New Zealand": "nz",
    "Nigeria": "ng",
    "Norway": "no",
    "Philippines": "ph",
    "Poland": "pl",
    "Portugal": "pt",
    "Romania": "ro",
    "Russia": "ru",
    "Saudi Arabia": "sa",
    "Serbia": "rs",
    "Singapore": "sg",
    "Slovakia": "sk",
    "Slovenia": "si",
    "South Africa": "za",
    "South Korea": "kr",
    "Sweden": "se",
    "Switzerland": "ch",
    "Taiwan": "tw",
    "Thailand": "th",
    "Turkey": "tr",
    "Ukraine": "ua",
    "United Arab Emirates": "ae",
    "United Kingdom": "gb",
    "United States": "us",
    "Venezuela": "ve"
}
    country_code = country_codes[country_name]
    articles = headline(country_code,category)
    if  articles!=None:
        displaynews(articles)
if __name__ == '__main__':
    runmain()
