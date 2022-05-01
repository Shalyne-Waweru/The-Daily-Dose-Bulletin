class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_SOURCES_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    NEWS_HEADLINES_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    NEWS_CATEGORY_BASE_URL = "https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey={}"

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True