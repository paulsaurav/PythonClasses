import requests
import json

def fetch_news(api_key, query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def parse_news(data):
    articles = data['articles']
    parsed_articles = []
    for article in articles:
        parsed_article = {
            'source': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'urlToImage': article['urlToImage'],
            'url': article['url'],
            'description': article['description'],
            'content': article['content'],
        }
        parsed_articles.append(parsed_article)
    return parsed_articles

def main():
    api_key = '525e9265a50247dfb0494d1c72bd45b8'
    query = 'Bitcoin'
    data = fetch_news(api_key, query)
    parsed_data = parse_news(data)


    for idx, article in enumerate(parsed_data, start=1):
        print(f"Article {idx}:")
        print(f"Source: {article['source']}")
        print(f"Author: {article['author']}")
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Image URL: {article['urlToImage']}")
        print(f"Description: {article['description']}")
        print(f"Content: {article['content']}")
        print()

if __name__ == "__main__":
    main()



#implement error handling (try,catch,except method)
#store all the fetched data to a csv
#add another parameter to the url and get the news e.g. sort by or date or etc.
#https://newsapi.org/v2/everything?q=tesla&from=2024-04-14&sortBy=publishedAt&apiKey=
        



