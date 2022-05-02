class Sources:
  '''
  Sources class to define News Sources Objects
  '''

  def __init__(self,name,description,url,country):
    self.name = name
    self.description = description
    self.url = url
    self.country = country
   
class Headlines:
  '''
  Headlines class to define Headline Objects
  '''

  def __init__(self,image,title,author,publishedAt,description,url):
      self.image = image
      self.title = title
      self.author = author
      self.publishedAt = publishedAt
      self.description = description
      self.url = url

class Articles:
  '''
  Articles class to define Article Objects
  '''

  def __init__(self,image,title,author,publishedAt,description,url):
      self.image = image
      self.title = title
      self.author = author
      self.publishedAt = publishedAt
      self.description = description
      self.url = url