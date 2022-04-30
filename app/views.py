from flask import render_template
from app import app
from .request import get_sources,get_headlines

@app.route('/')
def landing_page():
  '''
  View root page function that returns the index page and its data
  '''

  #Get the News Sources
  news_sources = get_sources()

  #Get the Headlines Sources
  news_headlines = get_headlines()

  return render_template('index.html', news_sources = news_sources, news_headlines = news_headlines)