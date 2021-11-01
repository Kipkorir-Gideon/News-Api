import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news = News('Yuri1','Yuri News','Facebook changed its parent name to Meta.','https://www.yurinews.com/section/news','technology')

    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.news.id,'Yuri1')
        self.assertEquals(self.news.name,'Yuri News')
        self.assertEquals(self.news.description,'Facebook changed its parent name to Meta.')
        self.assertEquals(self.news.url,'https://www.yurinews.com/section/news')
        self.assertEquals(self.news.category,'technology')