import tweepy
import threading
import tmdbsimple as tmdb
import os
import re

consumer_key = 'TXY0GkilvwVRvJnD1BWB1omfv'
consumer_secret = 'FvlisMwchzIAy44rTGRbRPiA4zDdZYFfnbRl9pT8H7KzxA84pu'
access_token = '1943787344-CCc0Dtl2lQsH3Z6z3SLqyuMJ8uadmtQt0u1OX2n'
access_token_secret = 'IwbLmUAfbIhx9T8Kdrg8Qs5okFsFBRZTs4hDqt1wm0AkM'


def hashtags():

    f = open("upcoming_movies.txt", 'r')
    MovieNameArray = []
    wordWithoutSpaceArray = []
    j = 0

    a = 0

    for i in f:
            perseString = i.split(",")
            word = re.sub("[^a-zA-Z1-9 " "]+", "", perseString[0])

            MovieNameArray.append(word)
            
            wordWithoutSpace = word.replace(" ","")
            wordWithoutSpaceArray.append(wordWithoutSpace)

    f.close         
    HashTagsFull = open("FullHashTags.txt", 'a+')

    for i in wordWithoutSpaceArray:

            HashTagsFull = open("FullHashTags.txt", 'r')

            for j in HashTagsFull:
                   if (i == j.rstrip("\n")):
                          a = 1 
            HashTagsFull.close()
            
            HashTagFileOpen = open ("FullHashTags.txt", 'a+')

            if (a !=1):
                    
                    HashTagFileOpen.write(i + "\n") 
            HashTagFileOpen.close()
                 
    HashTagsFull.close

    for i in MovieNameArray:
            a = 0
            HashTagsFull = open("FullHashTags.txt", 'r')
            for j in HashTagsFull:
                    if (i == j.rstrip("\n")):
                          a = 1
            HashTagsFull.close()
            HashTagFileOpen = open ("FullHashTags.txt", 'a+')
            if (a !=1):
                    
                    HashTagFileOpen.write(i + "\n")
            HashTagFileOpen.close()


    f.close()

def func1():
	tmdb.API_KEY = '38873c00e8dd14d801b2c1a57b5077c8'

	movie = tmdb.Movies()
	up = movie.upcoming()
	arr=[]
	arr2=[]
	up = up['results']
	for i in up:
		print i['title'], i['id'], i['release_date'], i['genre_ids']
		arr.append(i['title']+","+str(i['id'])+','+i['release_date'])

	if os.stat("upcoming_movies.txt").st_size == 0:
		f = open("upcoming_movies.txt", 'a+')
		for i in arr:
			f.write(i+"\n")
		f.close() 
	else:
		f = open("upcoming_movies.txt")
		for var in f:
			arr2.append(var.rstrip('\n'))
		f.close()
		for var2 in arr:
			if (var2 not in arr2):
				f= open("upcoming_movies.txt",'a')
				f.write(var2+"\n")
				f.close()

def func():
	func1()
	hashtags()
	f = open("FullHashTags.txt", 'r')
	arr = [i.rstrip("\n") for i in f]
	f.close()
	threading.Timer(21600, func).start()
	return arr

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
    	f =open("tweets.txt", 'a')
        #print(status.text, "<>" ,status.author.id, str(status.created_at))
        f.write(str(str(status.text).encode('utf-8')+ ";"+str(status.created_at).encode('utf-8')+"\n") )
        f.close()


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
arr = func()
myStream.filter(track = arr, languages=["en"])