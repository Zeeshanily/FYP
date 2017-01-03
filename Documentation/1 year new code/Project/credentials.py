import tweepy
from config import *

class Credentials():
    def API(self):
        config = Config()
        auth = tweepy.OAuthHandler(config.consumer_key() , config.consumer_secret())
        auth.set_access_token(config.access_token(), config.access_secret())
        api = tweepy.API(auth)

        return api