import tweepy
import time
import ids_collector_module
import credentials
from __inti__ import *
import Streaming_tweets 
import saveTweet

import loading_handlers
tech = []
politics = []
sports = []
all_handlers = []
entertainment = []
anchors = []

ld_hndlers = loading_handlers.Loading_Handlers()

tech = ld_hndlers.loading_handlers_in_array('techHandlers')
politics = ld_hndlers.loading_handlers_in_array('politicsHANDLERS')
sports = ld_hndlers.loading_handlers_in_array('sportsHANDLERS')
entertainment = ld_hndlers.loading_handlers_in_array('entertainmentHANDLERS')
anchor = ld_hndlers.loading_handlers_in_array('AnchorsHANDLERS')
News_channel = ld_hndlers.loading_handlers_in_array('News_channelHANDLERS')



api = credentials.Credentials().API()
mongo = creatingConnection()
Connection = mongo.run()
tweet = Streaming_tweets.Tweets()
save_Tweet = saveTweet.saveTweet()

def tweet_collections_by_handler(array, api, tag):
    a =1
    for i in range(0,len(array)):
        user_timeline = tweet.gathering_tweets(array[i], api)
        if((user_timeline != None)or (len(user_timeline) != 0)):
            save_Tweet.save_tweet(user_timeline, Connection, tag)
    return a

x=True
while(x==True):
    #tweet_collections_by_handler(sports, api, "Sports")
    #tweet_collections_by_handler(anchor, api, "Anchors")
    tweet_collections_by_handler(News_channel, api, "News_channel")
    tweet_collections_by_handler(entertainment, api, "Entertainment")
    tweet_collections_by_handler(tech, api, "Technology")
    tweet_collections_by_handler(politics, api, "Politics")
    

    
    x=False