import unittest
from TestSpider import TestSpider


import functions as fn


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.default_url = "https://www.google.com"
        cls.spider = TestSpider(url=cls.default_url)

    @classmethod
    def tearDownClass(cls):
        cls.spider.die()

    def setUp(self):
        self.spider.goto(self.default_url)
    
    def tearDown(self):
        pass

    def test_activation_time(self):
        pass
    
    def test_idle_time(self):
        pass

    def test_wait_between_intervals(self):
        pass



if __name__ == '__main__':
    unittest.main()
