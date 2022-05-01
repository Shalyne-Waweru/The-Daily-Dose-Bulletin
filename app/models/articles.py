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