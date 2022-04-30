import unittest
from models import news_sources

#Get the Sources Class 
Sources = news_sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','us')

    #FIRST TEST
    def test_instance(self):
        #The isinstance() function checks if the object self.new_source is an instance of the Sources class.
        self.assertTrue(isinstance(self.new_source,Sources))

    #SECOND TEST
    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      #The assertEqual() method checks for an expected result. 
      #The first argument is the expected result and the second argument is the result that is actually gotten. 
      self.assertEqual(self.new_source.name,"ABC News")
      self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
      self.assertEqual(self.new_source.url,"https://abcnews.go.com")
      self.assertEqual(self.new_source.country,"us")

if __name__ == '__main__':
    unittest.main()