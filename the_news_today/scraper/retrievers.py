import requests
import platform
from selenium import webdriver


def useRequests(url):
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return page.text

def usePhantom(url):
    if platform.system() == 'Windows':
        PHANTOMJS_PATH = './phantomjs.exe'
    else:
        PHANTOMJS_PATH = './scraper/phantomjs'

    browser = webdriver.PhantomJS(PHANTOMJS_PATH)
    browser.get(url)
    return browser.page_source
