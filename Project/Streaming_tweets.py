import time
import tweepy 
import datetime
import sys
 
counter = 0
x= True
class Tweets():
    def gathering_tweets(self, name, api, ids):
        tweets = []
        count = 0
        x=True
        global spe_id
        spe_id = ids
        #ids ='806539777201893377'
        endDate =   datetime.datetime(2015, 8, 1, 0, 0, 0)
        try:
            while(x==True):

                print "Gathering tweets"
                tweet_data = api.user_timeline(screen_name=name , max_id=spe_id, count=200)
                for tw in tweet_data:
                    if(tw.created_at> endDate):
                        tweets.append(tw)
                        print "tweet apended"
                        spe_id = tw.id_str
                    elif(tw.created_at< endDate):
                        return tweets
                    else:
                        print "Do nothing"
                print "sleeping for minute"
                time.sleep(60)
        except:
            print("Some problem occurs here. Code is resumed for 15 mins")
            time.sleep(900)



                #if(count == 200):
                #    print "Sleeping COde for 1 min to give API some rest"
                #    
                #    return tweets 

    #time.sleep(920) # 15 mins sleep is given ifrequests exceeds limit ... api should sleep for 15 mins because in 15 mins you are allowed to 15 requests onlyA
