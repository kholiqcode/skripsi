import tweepy as tw
from unidecode import unidecode


class Grab():
    def __init__(self):
        self.TWITTER_CONSUMER_KEY = '1jyHN0gmb7kOrPs7raCZuYwNZ'
        self.TWITTER_CONSUMER_SECRET = 'nrFnPcbVUAS7N1tHQowC08DdtHakyLr3vR1cEEhMRsbbwG02R7'
        self.TWITTER_ACCESS_TOKEN = '1215248323579236353-c1VL0Ti9bntvKPHNdX4vWjKvzxmrvB'
        self.TWITTER_ACCESS_TOKEN_SECRET = 'NachpxfacgvB1uQ5zfKli8seAvYkDHi0ULjqqXYEGSUb2'
        self.auth = tw.OAuthHandler(self.TWITTER_CONSUMER_KEY,
                                    self.TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(self.TWITTER_ACCESS_TOKEN,
                                   self.TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tw.API(self.auth, wait_on_rate_limit=True)

    @staticmethod
    def getTweetByKeyword(keyword,jumlah):
        tweets = tw.Cursor(Grab().api.search,
                           q=str(keyword)+" -filter:tweets",
                           lang="en").items(int(jumlah))
        # tweets = GrabController().api.search(
        #     q=keyword, lang="id", rpp=jumlah, tweet_mode='extended')
        tweetList = []
        for tweet in tweets:
            if('RT @' not in str(tweet.text)):
                fullText = str(tweet.text)
                userName = str(tweet.user.screen_name)
                tweetObj = {
                    "tweetid": tweet.id,
                    "userid": tweet.user.id,
                    "username": unidecode(userName),
                    "text": unidecode(fullText),
                    "label": 0,
                    "created_at": tweet.created_at,
                }
                tweetList.append(tweetObj)
        return tweetList

    @staticmethod
    def getTweetByUsername(username,jumlah=100):
        tweets = Grab().api.user_timeline(screen_name=username, count=jumlah)
        # tweets = GrabController().api.search(
        #     q=keyword, lang="id", rpp=jumlah, tweet_mode='extended')
        tweetList = []
        for tweet in tweets:
            if('RT @' not in str(tweet.text)):
                fullText = str(tweet.text)
                userName = str(tweet.user.screen_name)
                tweetObj = {
                    "tweetid": tweet.id,
                    "userid": tweet.user.id,
                    "username": unidecode(userName),
                    "text": unidecode(fullText),
                    "label": 0,
                    "created_at": tweet.created_at,
                }
                tweetList.append(tweetObj)
        return tweetList

    @staticmethod
    def getTweetByTag():
        tweets = Grab().api.available_trends()
        # tweets = GrabController().api.search(
        #     q=keyword, lang="id", rpp=jumlah, tweet_mode='extended')
        tweetList = []
        for tweet in tweets:
            if('RT @' not in str(tweet.text)):
                fullText = str(tweet.text)
                userName = str(tweet.user.screen_name)
                tweetObj = {
                    "tweetid": tweet.id,
                    "userid": tweet.user.id,
                    "username": unidecode(userName),
                    "text": unidecode(fullText),
                    "label": 0,
                    "created_at": tweet.created_at,
                }
                tweetList.append(tweetObj)
        return tweetList

    @staticmethod
    def getUserByUsername(username):
        user = Grab().api.get_user(screen_name=username)
        return user
