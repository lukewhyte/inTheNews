import datetime
from store.models import Headlines


class StoreHeadlines():
    """Validate and push returned data to DB
    """

    def __init__(self, retrieved):
        self.headlines = retrieved

    def getTimestamp(self):
        return datetime.datetime.now()

    def isDataValid(self):
        return any(headline[1] for headline in self.headlines)

    def buildDict(self):
        return { headline[0]: headline[1] for headline in self.headlines }

    def pushToDB(self):
        headlineHash = self.buildDict()
        timestamp = self.getTimestamp()

        headlines = Headlines(
            BBC=headlineHash['BBC'],
            CNN=headlineHash['CNN'],
            aljazeera=headlineHash['AlJazeera'],
            fox=headlineHash['Fox'],
            date=timestamp
        )
        headlines.save()
        return headlines

