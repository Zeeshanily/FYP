import json
import tweepy
import time

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

auth = tweepy.OAuthHandler('7IeaGKj3xuGpL4Qkm6Oy79rry','YhgmgDUPIbBiBhGtGKZkTcaacDATkl3XVaz1qysMHiNPgjOCoI')
auth.set_access_token('2240281597-wYZv8VBNpNZ7VU96sd65xkJo29DKIbBfK1hQKEH','PSkTKk4tH3oDsigkcHoPkkcjNKP3iHLxVODsUCukksEWE')

api = tweepy.API(auth)

place_id = "64a07f675a8a699a"

total = []
z = 0


while len(total) < 1000:
    user_timeline = api.user_timeline(screen_name="nabeelaq",count=200)
    for tweet in user_timeline:
        print "here"
        x = tweet._json
        print x
        tweet = json.dumps(tweet._json) + "\n"
        if(x['id'] in total):
            print "already exists"
            print "unique tweets: " + str(len(total))
        else:
            print "unique tweets: " + str(len(total))
            total.append(x['id'])
            o = open('handler.txt','a')
            o.write(tweet)
            o.close()
