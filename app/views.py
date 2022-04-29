from flask import render_template
from app import app

@app.route('/')
def landing_page():
  '''
  View root page function that returns the index page and its data
  '''

  return render_template('index.html')