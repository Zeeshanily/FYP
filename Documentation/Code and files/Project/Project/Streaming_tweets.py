import time
import tweepy 

class Tweets():
    def gathering_tweets(self, name, api):
        tweets = []
        count = 0
        try:
            for tweet in  tweepy.Cursor(api.user_timeline, id=name).items(200):
                print "Gathering Tweet: ", str(count)
                tweets.append(tweet)
                count += 1
                #if(count == 200):
                #    print "Sleeping COde for 1 min to give API some rest"
                #    time.sleep(60)
                #    return tweets 
            print "Sleeping COde for 1 min to give API some rest"
            time.sleep(60)
            return tweets

        except:
            print "Some problem occurs here. Code is resumed for 15 mins"
            time.sleep(920) # 15 mins sleep is given ifrequests exceeds limit ... api should sleep for 15 mins because in 15 mins you are allowed to 15 requests onlyA
            return tweets