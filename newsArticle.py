import requests

# your api key
API_KEY = ''

def newsArticle(api_key):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': 'us',  # put any country code you want
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']

        # Display the top headlines
        for i, article in enumerate(articles, start=1):
            print(f"Article {i}:")
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}")
            print()
    else:
        print(f"Error: Unable to generate news. Status code: {response.status_code}")

if __name__ == "__main__":
    newsArticle(API_KEY)
