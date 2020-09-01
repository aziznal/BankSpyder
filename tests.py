import unittest
from time import sleep, perf_counter
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
    
    def test_spider_stops_after_banks_close(self):
        # This test assumes banks are open
        pass


    def test_adjusted_interval(self):

        function_timer1 = perf_counter()

        interval = 5

        time1 = perf_counter()
        self.spider.refresh_page()
        time2 = perf_counter()

        adjusted_interval = fn.adjust_interval(time1, time2, interval)
        sleep(adjusted_interval)

        function_timer2 = perf_counter()
        total_sleep_time = round(function_timer2 - function_timer1, 4)

        self.assertAlmostEqual(total_sleep_time, interval, places=1)


if __name__ == '__main__':
    unittest.main()
