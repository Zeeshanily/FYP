from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

auth = tweepy.OAuthHandler('hRMv9piMGbvVJcxswTlCpFkWF','7abmYepyRepOaLSnIAiGpQfL4fuGU5XV5Ly7F105ah6fknTTT5')
auth.set_access_token('2536925046-vFL9U14kAQMhqjZslOOj1P2KIvFibOt5MBwbw1h','zcquEwII3yClJK9N4NCfNlVk4VtfcEKPbOghh5xYklKSU')

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            print "hit"
            with open('generic.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['PTI'])
