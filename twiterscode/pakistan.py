import json
import tweepy
import time

auth = tweepy.OAuthHandler('hRMv9piMGbvVJcxswTlCpFkWF','7abmYepyRepOaLSnIAiGpQfL4fuGU5XV5Ly7F105ah6fknTTT5')
auth.set_access_token('2536925046-vFL9U14kAQMhqjZslOOj1P2KIvFibOt5MBwbw1h','zcquEwII3yClJK9N4NCfNlVk4VtfcEKPbOghh5xYklKSU')
    
api = tweepy.API(auth)
#places = api.geo_search(query="Pakistan", granularity="country")
#place id for pakistan
place_id = "64a07f675a8a699a"
#enter keyword before place
total=[]
z=0

while len(total) <1000:
    searched_tweets = [status for status in tweepy.Cursor(api.search,q="PTI:%s" % place_id).items(2000)]
    for i in searched_tweets:
        z+=1
        print "total fetched tweets: "+str(z)
        x= i._json
        i=json.dumps(i._json)+"\n"
        if (x['id'] in total):
            print "already exists"
            print "unique tweets: "+str(len(total))
        else:
            print "unique tweets: "+str(len(total))
            total.append(x['id'])
            o=open('pakistan.txt','a')
            o.write(i)
            o.close()
 
