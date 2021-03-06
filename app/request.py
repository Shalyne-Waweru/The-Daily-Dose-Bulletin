#Contains the code to make requests to our API.
import urllib.request,json

from .models import Sources
from .models import Headlines
from .models import Articles

# Getting api key
api_key = None

# Getting the news sources base url
news_sources_base_url = None

# Getting the news headlines base url
news_headlines_base_url = None

# Getting the news categories base url
news_categories_base_url = None

def configure_request(app):
    global api_key,news_sources_base_url,news_headlines_base_url,news_categories_base_url

    api_key = app.config['NEWS_API_KEY']
    news_sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
    news_headlines_base_url = app.config['NEWS_HEADLINES_BASE_URL']
    news_categories_base_url = app.config['NEWS_CATEGORY_BASE_URL']

#-------------------->Create a get_sources function
def get_sources():
  '''
  Function that gets the json response to our url request
  '''

  #The format()method will replace the {} curly brace placeholders in the news_sources_base_url with the api_key.
  # https://newsapi.org/v2/top-headlines/sources?apiKey={}
  get_news_sources_url = news_sources_base_url.format(api_key)

  with urllib.request.urlopen(get_news_sources_url) as url:
    #Use the read() function to read the response and store it in a get_sources_data variable.
    get_sources_data = url.read()

    #Convert the JSON response to a Python dictionary using json.loads function
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    #Checking if the response contains any data
    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']

      #If it does we call a process_results() function
      sources_results = process_results(sources_results_list)

  return sources_results

#The function takes in the list of dictionary objects and returns a list of news sources objects.
def process_results(sources_list):
  '''
  Function that processes the sources result and transform them to a list of Objects

  Args:
      sources_list: A list of dictionaries that contain news sources details

  Returns :
      sources_results: A list of news sources objects
  '''

  #Create an empty list to store our newly created news sources objects.
  sources_results = []

   #Loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values.
  for headline in sources_list:
    name = headline.get('name')
    description = headline.get('description')
    url = headline.get('url')
    country = headline.get('country')

    #Creating the news headline objects and append it to the empty list
    news_source_object = Sources(name,description,url,country)
    sources_results.append(news_source_object)

  return sources_results

#----------------------->Create a get_headlines function
def get_headlines():
  '''
  Function that gets the json response to our url request
  '''

  # The format()method will replace the {} curly brace placeholders in the news_headlines_base_url with the api_key.
  # https://newsapi.org/v2/top-headlines?country=us&apiKey={}
  get_news_headlines_url = news_headlines_base_url.format(api_key)

  with urllib.request.urlopen(get_news_headlines_url) as url:
    #Use the read() function to read the response and store it in a get_headlines_data variable.
    get_headlines_data = url.read()

    #Convert the JSON response to a Python dictionary using json.loads function
    get_headlines_response = json.loads(get_headlines_data)

    headlines_results = None

    #Checking if the response contains any data
    if get_headlines_response['articles']:
      headlines_results_list = get_headlines_response['articles']

      #If it does we call a process_results() function
      headlines_results = process_headline_results(headlines_results_list)

  return headlines_results

#The function takes in the list of dictionary objects and returns a list of news headlines objects.
def process_headline_results(headlines_list):
  '''
  Function that processes the headlines result and transform them to a list of Objects

  Args:
      headlines_list: A list of dictionaries that contain news headlines details

  Returns :
      headlines_results: A list of news headlines objects
  '''

  #Create an empty list to store our newly created news headlines objects.
  headlines_results = []

   #Loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values.
  for headline in headlines_list:
    image = headline.get('urlToImage')
    title = headline.get('title')
    author = headline.get('author')
    publishedAt = headline.get('publishedAt')
    description = headline.get('description')
    url = headline.get('url')

    if image:
      #Creating the news headline objects and append it to the empty list
      news_headline_object = Headlines(image,title,author,publishedAt,description,url)
      headlines_results.append(news_headline_object)

  return headlines_results

#------------------------>Create a get_articles function
def get_articles(category):
  '''
  Function that gets the json response to our url request
  '''

  #The format()method will replace the {} curly brace placeholders in the news_sources_base_url with the category and api_key.
  get_news_articles_url = news_categories_base_url.format(category,api_key)

  with urllib.request.urlopen(get_news_articles_url) as url:
    #Use the read() function to read the response and store it in a get_articles_data variable.
    get_articles_data = url.read()

    #Convert the JSON response to a Python dictionary using json.loads function
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    #Checking if the response contains any data
    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']

      #If it does we call a process_results() function
      articles_results = process_articles_results(articles_results_list)

  return articles_results

#The function takes in the list of dictionary objects and returns a list of news articles objects.
def process_articles_results(articles_list):
  '''
  Function that processes the articles result and transform them to a list of Objects

  Args:
      articles_list: A list of dictionaries that contain news articles details

  Returns :
      articles_results: A list of news articles objects
  '''

  #Create an empty list to store our newly created news articles objects.
  articles_results = []

  #Loop through the list of dictionaries using the get() method and pass in the keys so that we can access the values.
  for article in articles_list:
    image = article.get('urlToImage')
    title = article.get('title')
    author = article.get('author')
    publishedAt = article.get('publishedAt')
    description = article.get('description')
    url = article.get('url')

    if image:
      #Creating the news article objects and append it to the empty list
      news_article_object = Articles(image,title,author,publishedAt,description,url)
      articles_results.append(news_article_object)

  return articles_results