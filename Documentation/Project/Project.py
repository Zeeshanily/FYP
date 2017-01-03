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

tech_ids = []

politics_ids = []

sports_ids = []

entertainment_ids = []

anchors_ids = []

News_channel_ids= []

ld_hndlers = loading_handlers.Loading_Handlers()

id_coll = ids_collector_module.ids_collector()


#tech = ld_hndlers.loading_handlers_in_array('techHandlers')
#politics = ld_hndlers.loading_handlers_in_array('politicsHANDLERS')
#sports = ld_hndlers.loading_handlers_in_array('sportsHANDLERS')
#entertainment = ld_hndlers.loading_handlers_in_array('entertainmentHANDLERS')
anchor = ld_hndlers.loading_handlers_in_array('AnchorsHANDLERS')
News_channel = ld_hndlers.loading_handlers_in_array('News_channelHANDLERS')

api = credentials.Credentials().API()
mongo = creatingConnection()
Connection = mongo.run()
tweet = Streaming_tweets.Tweets()
save_Tweet = saveTweet.saveTweet()

def pick_first_ids( api):
    a = 1
    global tech_ids, politics_ids, sports_ids, entertainment_ids, anchors_ids, News_channel_ids

    #tech_ids  =id_coll.collector(tech, api)
    #politics_ids = id_coll.collector(politics, api)
    #sports_ids = id_coll.collector(sports, api)
    #entertainment_ids = id_coll.collector(entertainment, api)
    anchors_ids = id_coll.collector(anchor, api)
    News_channel_ids= id_coll.collector(News_channel, api)
    return a


def tweet_collections_by_handler(array, arr_id, api, tag):
    #j = 0
    global tech_ids, politics_ids, sports_ids, entertainment_ids, anchors_ids, News_channel_ids
    for i in range(0,len(array)-1):
        try:
            [user_timeline, retid] = tweet.gathering_tweets(array[i], api, arr_id[i])
            if(retid != None):
                if(array[len(array)-1]=='techHANDLERS'):
                    tech_ids[i]=retid
                elif(array[len(array)-1]=='politicsHANDLERS'):
                    politics_ids[i]=retid
                elif(array[len(array)-1]=='AnchorsHANDLERS'):
                    anchors_ids[i]=retid
                elif(array[len(array)-1]=='News_channelHANDLERS'):
                    News_channel_ids[i]=retid
                elif(array[len(array)-1]=='SportsHANDLERS'):
                    sports_ids[i]=retid
                else:
                    entertainment_ids[i]=retid
            if(user_timeline != None):
                save_Tweet.save_tweet(user_timeline, Connection, tag)
        except:
            print "Do nothing"

pick_first_ids(api)
while(1==1):
    #tweet_collections_by_handler(politics,politics_ids, api, "Politics")
    #tweet_collections_by_handler(sports,sports_ids, api, "Sports")
    #tweet_collections_by_handler(entertainment,entertainment_ids, api, "Entertainment")
    tweet_collections_by_handler(anchor, anchors_ids, api, "Anchors")
    tweet_collections_by_handler(News_channel, News_channel_ids, api, "News_channel")
    #tweet_collections_by_handler(tech,tech_ids, api, "Technology")