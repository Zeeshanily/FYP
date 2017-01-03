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
global tech_ids
tech_ids = []
global politics_ids
politics_ids = []
global sports_ids
sports_ids = []
global entertainment_ids
entertainment_ids = []
global anchors_ids
anchors_ids = []
global News_channel_ids
News_channel_ids= []

ld_hndlers = loading_handlers.Loading_Handlers()

id_coll = ids_collector_module.ids_collector()


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
def ids_collect( api):
    tech_ids  =id_coll.collector(tech, api)
    politics_ids = id_coll.collector(politics, api)
    sports_ids = id_coll.collector(sports, api)
    entertainment_ids = id_coll.collector(entertainment, api)
    anchors_ids = id_coll.collector(anchor, api)
    News_channel_ids= id_coll.collector(News_channel, api)

ids_collect(api)
def tweet_collections_by_handler(array, arr_id, api, tag):
    j = 0
    for i in range(0,len(array)):

        user_timeline = tweet.gathering_tweets(array[i], api, arr_id[j])
        j = j+1
        if(user_timeline != None):
            save_Tweet.save_tweet(user_timeline, Connection, tag)


tweet_collections_by_handler(tech,tech_ids, api, "Technology")
tweet_collections_by_handler(politics,politics_ids, api, "Politics")
tweet_collections_by_handler(sports,sports_ids, api, "Sports")
tweet_collections_by_handler(entertainment,entertainment_ids, api, "Entertainment")
tweet_collections_by_handler(anchor, anchors_ids, api, "Anchors")
tweet_collections_by_handler(News_channel, News_channel_ids, api, "News_channel")