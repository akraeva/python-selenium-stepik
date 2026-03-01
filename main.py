from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)
