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
    title = "Various News fro Around The Globe"


    return render_template('index.html', title = title, business = business, technology = technology, entertainment = entertainment, sports = sports) 