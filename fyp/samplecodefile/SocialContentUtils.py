from models.SocialContent import *
from models.SocialProfile import *
from models.customRefs.Author import *
from models.fieldvalues.SocialHostValues import *
from models.fieldvalues.SocialProfileAttributes import *
from models.fieldvalues.SocialContentValues import *
from datetime import datetime

class SocialContentUtils(object):

	# def getLastTweet(object, socialProfile):
		# tweets = SocialContent.objects("author.sId" = socialProfile.id)
		# if tweets.count() == 0:
		# 	return null
		# else:
		# 	return tweets[0]
			

	def createOrUpdateSocialContent(object,post, socialProfile, source_content_type = SocialContentValues.TWITTER_TWEET):
		sId =  str(post['id']) if socialProfile.h == SocialHostValues.TWITTER else str(post['id']) 
		socialContents = SocialContent.objects(sId=sId)
		if socialContents.count() != 0:
			socialContent = socialContents.first()
		else:
			socialContent = SocialContent()	
			
		if socialProfile.h == SocialHostValues.TWITTER:
			return SocialContentUtils.processSocialContent(SocialContentUtils(),post,socialProfile,socialContent,source_content_type)
		else:
			return SocialContentUtils.processFacebookSocialContent(SocialContentUtils(),post,socialProfile,socialContent,source_content_type)		
		
	def processFacebookSocialContent(object, post, socialProfile, socialContent, source_content_type):
		print post
		socialContent.h 	= socialProfile.h
		socialContent.sId 	= str(post['id'])
		socialContent.sCT   = source_content_type
		socialContent.t 	= post['message']
		socialContent.u 	= post['link'] if 'link' in post else '' 
		socialContent.pSId  = ''
		socialContent.author = Author(uN = socialProfile.n, n = socialProfile.n, sId = socialProfile.sId, iU = socialProfile.iU)
		socialContent.social_profile_id = socialProfile.id
		socialContent.cD = datetime.strptime(post['created_time'],"%Y-%m-%dT%H:%M:%S+0000") 
		socialContent.save()
		print "Tweet Saved " 
		return socialContent		
					

	def processSocialContent(object, tweet, socialProfile, socialContent, source_content_type):
		socialContent.h 	= SocialHostValues.TWITTER
		socialContent.sId 	= tweet['id_str']
		socialContent.sCT   = source_content_type
		socialContent.t 	= tweet['text']
		socialContent.u 	= '' if source_content_type == SocialContentValues.DIRECT_MESSAGE else tweet['source']
		socialContent.pSId  = '' if source_content_type == SocialContentValues.DIRECT_MESSAGE else tweet['in_reply_to_status_id_str']
		socialContent.author = Author(uN = socialProfile.uN, n = socialProfile.n, sId = socialProfile.sId, iU = socialProfile.iU)
		socialContent.social_profile_id = socialProfile.id

		rcps = []
		if source_content_type == SocialContentValues.DIRECT_MESSAGE:
			recipient_id = tweet['recipient_id']
			if recipient_id not in rcps:
				rcps.append(str(recipient_id))
		else:
			tweet_rcps = tweet['entities']['user_mentions']
			if (len(tweet_rcps) > 0):
				for rcp in tweet_rcps:
					if rcp['id_str'] not in rcps:
						rcps.append(rcp['id_str'])

		socialContent.rcps 	= rcps
		socialContent.save()
		print "Tweet Saved " 
		return socialContent

	def processForStreams(object, tweet, streamInclusionToIdMap):
		if len(streamInclusionToIdMap) > 0 :
			for word, streamId in streamInclusionToIdMap.iteritems():
				tweet_text = tweet.t.lower().strip()
				word = word.lower().strip()
				print "word -->> " + word
				print "tweet -->> " + tweet_text
				print "check -->> " + str(word in tweet_text)
				print "check -->> " + str(streamId  not in tweet.clA)
				print "check -->> " + str(tweet.clsA)
				if word in tweet_text:
					if streamId  not in tweet.clA:
						tweet.clsA.append(streamId)
			tweet.save()
		return tweet



