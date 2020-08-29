# Import your Spyder here
from TestSpyder import TestSpyder
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():
    
    url = 'https://www.google.com'

    options = FirefoxOptions()
    options.headless = False

    # TODO: replace with an instance of your bank spyder
    spyder = TestSpyder(url=url, options=options)

    return spyder
