import scrapers
import retrievers
from storage import StoreHeadlines


class GetTheNews():
    """Control class for managing all scraper operations
    """

    def __init__(self):
        self.outlets = self.getOutlets()

    def getOutlets(self):
        return [
            { 
                'url': 'http://www.bbc.com/news/world',
                'scraper': scrapers.BBC,
                'name': 'BBC',
                'retriever': retrievers.useRequests
            },
            { 
                'url': 'http://www.foxnews.com/',
                'scraper': scrapers.fox,
                'name': 'Fox',
                'retriever': retrievers.useRequests,
            },
            { 
                'url': 'http://edition.cnn.com/',
                'scraper': scrapers.CNN,
                'name': 'CNN',
                'retriever': retrievers.usePhantom,
            },
            { 
                'url': 'http://www.aljazeera.com/',
                'scraper': scrapers.aljazeera,
                'name': 'AlJazeera',
                'retriever': retrievers.useRequests,
            }
        ]

    def runScrapers(self):
        retrieved = []
        for outlet in self.outlets:
            raw = outlet['retriever'](outlet['url'])
            if raw is not None:
                headline = outlet['scraper'](raw)
                retrieved.append((outlet['name'], headline))
            else:
                retrieved.append((outlet['name'], None))
        self.attemptStorage(retrieved)

    def attemptStorage(self, retrieved):
        storeHeadlines = StoreHeadlines(retrieved)
        if storeHeadlines.isDataValid():
            storeHeadlines.pushToDB()
