from bs4 import BeautifulSoup


from Locators.tweetsLocator import TweetsLocators
from Parser.tweetParser import TweetParser
import time


class Tweet:


    def __init__(self, page):
        self.page = "YOUR URL"
        self.soup = BeautifulSoup(self.page, 'html.parser')




    @property
    def tweets_split(self):
        locator = TweetsLocators.TWEET
        tweets_tags = self.soup.select_one(locator)

        return [TweetParser(e) for e in tweets_tags]

