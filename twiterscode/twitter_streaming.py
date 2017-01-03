#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2536925046-vFL9U14kAQMhqjZslOOj1P2KIvFibOt5MBwbw1h"
access_token_secret = "zcquEwII3yClJK9N4NCfNlVk4VtfcEKPbOghh5xYklKSU"
consumer_key = "hRMv9piMGbvVJcxswTlCpFkWF"
consumer_secret = "7abmYepyRepOaLSnIAiGpQfL4fuGU5XV5Ly7F105ah6fknTTT5"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
