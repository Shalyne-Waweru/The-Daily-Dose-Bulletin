#Contains the code to make requests to our API.
from app import app
import urllib.request,json
from .models import news_sources

Sources = news_sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news sources base url
news_sources_base_url = app.config['NEWS_SOURCES_BASE_URL']

#Create a get_sources function
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
  for source in sources_list:
    name = source.get('name')
    description = source.get('description')
    url = source.get('url')
    country = source.get('country')

    #Creating the news source objects and append it to the empty list
    news_source_object = Sources(name,description,url,country)
    sources_results.append(news_source_object)

  return sources_results