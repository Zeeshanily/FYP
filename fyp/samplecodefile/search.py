import tweepy
import time
import sys, time
from daemon import Daemon
import re
from utils.SocialProfileUtils import *
from utils.SocialContentUtils import *
from utils.StreamUtils import *
import time
import json
import config
from models.Streams import *

class SearchDaemon(Daemon):
	def run(self):
		auth = tweepy.OAuthHandler(config.ckey, config.csecret)
		auth.set_access_token(config.atoken, config.asecret)
		api =  tweepy.API(auth)
		ids = []
		# getting streams
		streams = Streams.objects()
		stream_titles = []
		for document in streams:
			stream_titles += document.inclusion.split(",")
			# stream_titles.append(document.inclusion)
		query = ' OR '.join(stream_titles) #str(v) for v in stream_titles)
		print query
		print "\n ========\n"

		for tweet in tweepy.Cursor(api.search, q = query).items():
			#for tweet in tweepy.Cursor(api.search, q = query).items():
			socialProfile = SocialProfileUtils.createOrUpdateSocialProfile(SocialProfileUtils(), tweet.user.__dict__)
			status = tweet.__dict__
			socialContent = SocialContentUtils.createOrUpdateSocialContent(SocialContentUtils(),status, socialProfile)
			socialContent = SocialContentUtils.processForStreams(SocialContentUtils(),socialContent, StreamUtils.getStreamInclusionMap(StreamUtils()))

			time.sleep(60)

if __name__ == "__main__":
        daemon = SearchDaemon('/tmp/search-daemon.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)