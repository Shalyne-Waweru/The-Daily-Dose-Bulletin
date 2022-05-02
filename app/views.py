from flask import render_template
from app import app
from .request import get_sources,get_headlines,get_articles

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

@app.route('/top-headlines?category=technology')
def tech_page():
  '''
  View tech_page function that returns the tech page and its data
  '''

  #Get the News Articles
  news_articles = get_articles('technology')

  return render_template('tech_page.html', news_articles = news_articles)

@app.route('/top-headlines?category=business')
def business_page():
  '''
  View business_page function that returns the business page and its data
  '''

  #Get the News Articles
  news_articles = get_articles('business')

  return render_template('business_page.html', news_articles = news_articles)

@app.route('/top-headlines?category=entertainment')
def entertainment_page():
  '''
  View entertainment_page function that returns the entertainment page and its data
  '''

  #Get the News Articles
  news_articles = get_articles('entertainment')

  return render_template('ent_page.html', news_articles = news_articles)

