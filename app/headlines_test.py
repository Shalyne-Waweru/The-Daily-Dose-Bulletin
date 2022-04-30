import unittest
from models import headlines

#Get the Headlines Class 
Headlines = headlines.Headlines

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Headlines class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headline = Headlines('https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2021%2F0805%2Fr891675_1296x729_16%2D9.jpg','New York Jets brass downplays unfamiliar praise for NFL draft class - ESPN','Rich Cimini','2022-04-30T20:38:51Z','The Jets are shrugging off universal praise for their draft class','https://www.espn.com/nfl/story/_/id/33833640/new-york-jets-brass-downplays-uncommon-praise-nfl-draft-class')

    #FIRST TEST
    def test_instance(self):
        #The isinstance() function checks if the object self.new_headline is an instance of the Headlines class.
        self.assertTrue(isinstance(self.new_headline,Headlines))

    #SECOND TEST
    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      #The assertEqual() method checks for an expected result. 
      #The first argument is the expected result and the second argument is the result that is actually gotten. 
      self.assertEqual(self.new_headline.image,"https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2021%2F0805%2Fr891675_1296x729_16%2D9.jpg")
      self.assertEqual(self.new_headline.title,"New York Jets brass downplays unfamiliar praise for NFL draft class - ESPN")
      self.assertEqual(self.new_headline.author,"Rich Cimini")
      self.assertEqual(self.new_headline.publishedAt,"2022-04-30T20:38:51Z")
      self.assertEqual(self.new_headline.description,"The Jets are shrugging off universal praise for their draft class")
      self.assertEqual(self.new_headline.url,"https://www.espn.com/nfl/story/_/id/33833640/new-york-jets-brass-downplays-uncommon-praise-nfl-draft-class")

if __name__ == '__main__':
    unittest.main()