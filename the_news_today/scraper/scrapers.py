from bs4 import BeautifulSoup


def BBC(raw):
    html = BeautifulSoup(raw, 'html.parser')
    try:
        parent = html.find('h3', 'title-link__title')
        headline = parent.find('span')
    except:
        return None
    return headline.get_text()

def fox(raw):
    html = BeautifulSoup(raw, 'html.parser')
    try:
        parent = html.find('div', id='big-top').find('div', 'primary')
        headline = parent.h1.a
    except:
        return None
    return headline.get_text()

def CNN(raw):
    html = BeautifulSoup(raw, 'html.parser')
    try:
        headline = html.find('h2')
    except:
        return None
    return headline.get_text()

def aljazeera(raw):
    html = BeautifulSoup(raw, 'html.parser')
    try:
        headline = html.find('h1', 'top-sec-title')
    except:
        return None
    return headline.get_text()
