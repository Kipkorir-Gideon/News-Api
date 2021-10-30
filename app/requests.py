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

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news(news_results_list)

    return news_results

def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        news_object = News(id,name,description,url,category)
        news_results.append(news_object)

    return news_results

def get_articles(id):
    '''
    Method that processes the articles and returns a list of articles object
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())


        article_object = None
        if articles_results['articles']:
            article_object = process_articles(articles_results['articles'])

    return article_object

def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of articles objects
    '''

    articles_list = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_results = Articles(id,author,title,description,url,image,date)
            articles_list.append(articles_results)

    return articles_results