import time
import tweepy 
import datetime
import sys
 
counter = 0
x= True
class Tweets():
    def gathering_tweets(self, name, api):
        #time.sleep(120)
        print name 
        user_timeline = []
        tweets = []
        try:
            user_timeline = api.user_timeline(screen_name=name ,count=1)
            ids = user_timeline[0].id_str
            time.sleep(60)
        except:
            print "Some error has come here initally"
            return tweets
        
        count = 0
        x=True
        
        spe_id = ids
        chk =0
        endDate =   datetime.datetime(2015, 8, 1, 0, 0, 0)
        try:
            while(x==True):
                #count = 0
                
                tt=0
                print "here is your id"+str(spe_id)
                print "Gathering tweets"
                tweet_data = api.user_timeline(screen_name=name , max_id=spe_id, count=200)
                print "Size Chunks of tweet: "+str(len(tweet_data))
                if((len(tweet_data)==0) or (len(tweet_data)== 1)):
                    print "due to small size in data it is returning"
                    return tweets
                for tw in tweet_data:
                
                    #tt= tt+1
                    #print "gather#" + str(tt)
                    #a = tw.id_str

                    #f = open('myfile.txt','a')
                    #f.write(name+'\t' +a+'\n' ) # python will convert \n to os.linesep
                    #f.close()
                    #if(tweet_data[len(tweet_data)-1].id_str==tw.id_str):
                    #    print "due to redundance you are terminating"
                        #f = open('myfile.txt','a')
                        #f.write('Zeeshan ' '\t' '1234''\n' ) # python will convert \n to os.linesep
                        #f.close()

                    #    return tweets


                    if(tw.created_at> endDate):
                        tweets.append(tw)
                        print "tweet apended size: "+str(len(tweets))
                        count =count+1
                        print count
                        spe_id = tw.id_str
                        
                    if(tw.created_at< endDate):
                        print "due to date you are terminating"
                        return tweets
                    
                    if(len(tweets) >3200):
                        return tweets
                
                    else:
                        print "Do nothing"
                
                print "sleeping for minute api is resting here"
                time.sleep(60)
        except:
            print("Some problem occurs here. Code is resumed for 15 mins")

            time.sleep(900)
            return tweets