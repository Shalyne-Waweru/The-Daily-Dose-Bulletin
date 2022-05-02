import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('https://content.fortune.com/wp-content/uploads/2022/05/AP22119837202554.jpg?resize=1200,600','Elon Musk’s big plans for Twitter: What we know so far - Fortune','Matt O\'Brien, The Associated Press','2022-05-01T20:00:12Z','Tesla CEO Elon Musk has laid out some bold, if still vague','https://fortune.com/2022/05/01/elon-musks-big-plans-for-twitter-what-we-know-so-far/')

    #FIRST TEST
    def test_instance(self):
        #The isinstance() function checks if the object self.new_article is an instance of the Articles class.
        self.assertTrue(isinstance(self.new_article,Articles))

    #SECOND TEST
    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      #The assertEqual() method checks for an expected result. 
      #The first argument is the expected result and the second argument is the result that is actually gotten. 
      self.assertEqual(self.new_article.image,"https://content.fortune.com/wp-content/uploads/2022/05/AP22119837202554.jpg?resize=1200,600")
      self.assertEqual(self.new_article.title,"Elon Musk’s big plans for Twitter: What we know so far - Fortune")
      self.assertEqual(self.new_article.author,"Matt O'Brien, The Associated Press")
      self.assertEqual(self.new_article.publishedAt,"2022-05-01T20:00:12Z")
      self.assertEqual(self.new_article.description,"Tesla CEO Elon Musk has laid out some bold, if still vague")
      self.assertEqual(self.new_article.url,"https://fortune.com/2022/05/01/elon-musks-big-plans-for-twitter-what-we-know-so-far/")
