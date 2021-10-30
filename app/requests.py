import urllib.request,json
from .models import News,Articles
from datetime import date

#Getting the api key
api_key = None

#Getting News base url
base_url = None

#Getting Articles url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_BASE_URL']
    articles_url = app.config['ARTICLE_BASE_URL']

