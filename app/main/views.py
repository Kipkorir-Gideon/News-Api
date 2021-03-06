from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import News


#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting news sources
    business = get_news('business')
    technology = get_news('technology')
    entertainment = get_news('entertainment')
    sports = get_news('sports')
    title = "Global News"


    return render_template('index.html', title = title, business = business, technology = technology, entertainment = entertainment, sports = sports) 


@main.route('/articles/<id>')
def articles(id):
    '''
    View articles page function that returns the articles page and its data
    '''
    articles = get_articles(id)
    title = f'Articles from the News site | {id}'

    return render_template('articles.html',title = title, articles = articles)