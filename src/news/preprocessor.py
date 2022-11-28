from newsapi import NewsApiClient
from decouple import config

if __name__ == "__main__":
    # Init
    api = NewsApiClient(api_key=config("NEWS_API_KEY"))
    print(api.get_top_headlines())

