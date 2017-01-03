# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:25:16 2016

@author: mubashir
"""

# pip install twython

from twython import Twython 

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''


CONSUMER_KEY = "tLOTg3d0XpEE3HvtoqfMyuch9"
CONSUMER_SECRET = "2hsw6Krqt4KdC0IKxMPmkoFNM2g1Z2nxaOHdyKMWlaYMMeRtII"
OAUTH_TOKEN = "201701035-ZtO9FQzBMPua0mahwn1eUYkV77vdqtIRheX1r4Tf"
OAUTH_TOKEN_SECRET = "ItdOu4PDx8wG5fFhJS8jk5WB2VK16zQ2lW6jR2FasJvXP"
twitter = Twython(
        CONSUMER_KEY, CONSUMER_SECRET,
        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        
counter = 0;
        
lis = [798987394838097922] 

user_timeline = twitter.get_user_timeline(screen_name="BillGates",
    count=200, include_retweets=False, max_id=lis[-1])
    

for tweet in user_timeline:
        print (tweet['text']) 
        print("\n\n")
        counter+=1
        lis.append(tweet['id']) 

print(counter)