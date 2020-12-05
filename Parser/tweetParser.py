from Locators.tweetContentLocator import TweetContentLocator

class TweetParser:
    def __int__(self, tweet_tag):
        self.tweet_tag = tweet_tag


    @property
    def tweet_data(self):
        locator = TweetContentLocator.TWEET
        return self.parent.select_one(locator).string
    @property
    def nb_retweet(self):
        locator = TweetContentLocator.NB_RETWEETS
        return self.parent.select_one(locator).string
    @property
    def replies(self):
        locator = TweetContentLocator.REPLY
        return self.parent.select_one(locator).string


