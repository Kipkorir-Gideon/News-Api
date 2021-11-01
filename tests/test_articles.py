import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Yuri2','Yuri Gagari','From Facebook to Meta','Facebook has changed its parent name to Meta. This is, they said, to reflect the vision of the company.','https://www.yurinews.com/news/facebook-meta','meta.jpg','2021-10-31T06:43:22Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'Yuri2')
        self.assertEquals(self.new_article.author,'Yuri Gagari')
        self.assertEquals(self.new_article.title,'From Facebook to Meta')
        self.assertEquals(self.new_article.description,'Facebook has changed its parent name to Meta. This is, they said, to reflect the vision of the company.')
        self.assertEquals(self.new_article.url,'https://www.yurinews.com/news/facebook-meta')
        self.assertEquals(self.new_article.image,'meta.jpg')
        self.assertEquals(self.new_article.date,'2021-10-31T06:43:22Z')