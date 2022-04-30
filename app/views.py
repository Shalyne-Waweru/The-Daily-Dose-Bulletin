from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def landing_page():
  '''
  View root page function that returns the index page and its data
  '''

  #Get the News Sources
  news_sources = get_sources()

  return render_template('index.html', news_sources = news_sources)