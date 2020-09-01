from BankSpider import BankSpider
from selenium.webdriver.firefox.options import Options as FirefoxOptions


default_options = FirefoxOptions()
default_options.headless = False


class TestSpider(BankSpider):
    def __init__(self, options=default_options, *args, **kwargs):
        super().__init__(options=default_options, *args, **kwargs)

        self.active = False

    def get_single_reading(self):
        return (1, 2, 3, 4)

    def wait_till_next_interval(self):
        # TODO: implement
        pass
