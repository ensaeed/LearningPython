
from selenium import webdriver

def test_basic_options():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get('https://www.carcheck.co.uk/')
    print(driver.page_source)

test_basic_options()