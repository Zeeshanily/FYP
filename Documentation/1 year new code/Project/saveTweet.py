import social_Content
#import Author
import datetime
#import getting_data_from_db 


#db_data = getting_data_from_db.db_data()
#all_db_id = db_data.get_ids_db()
class saveTweet():
    def save_tweet(self, user_timeline, connection, tag_tweet):
        #all_db_id =all_db_id
        count = 0
        try:
            #for post in  social_Content.social_content.objects:
            #    mylst.append(post.id1)
            for tweet in user_timeline:
                try:
                    count1 = social_Content.social_content.objects(id1=tweet.id).count()
                    print count1
                    if ( count1 >= 1):
                        print "Already exist"
                    else:
                        socialContent = social_Content.social_content()
                        socialContent.created_at = tweet.created_at
                        socialContent.id1 = tweet.id
                        socialContent.id_str = tweet.id_str.encode('utf-8')
                        socialContent.text = tweet.text.encode('utf-8')
                        socialContent.source = tweet.source.encode('utf-8')
                        socialContent.i_r_t_s_i = tweet.in_reply_to_status_id
                        socialContent.i_r_t_s_i_s = tweet.in_reply_to_status_id_str
                        socialContent.i_r_t_u_i = tweet.in_reply_to_user_id
                        socialContent.i_r_t_u_i_s = tweet.in_reply_to_user_id_str
                        socialContent.i_r_t_s_n = tweet.in_reply_to_screen_name
                        socialContent.general_tags = tag_tweet
                        socialContent.author = social_Content.Author(profile_image_url = tweet.user.profile_image_url, statuses_count= tweet.user.statuses_count, favourites_count= tweet.user.favourites_count, listed_count = tweet.user.listed_count, description = tweet.user.description, location =  tweet.user.location, verified = tweet.user.verified, followers_count = tweet.user.followers_count, url = tweet.user.url, geo_enabled= tweet.user.geo_enabled, frs= tweet.user.follow_request_sent, frcnt = tweet.user.friends_count, uid1 =  tweet.user.id , id_str = tweet.user.id_str, name = tweet.user.name, screen_name = tweet.user.screen_name, lang = tweet.user.lang, time_zone = tweet.user.time_zone, created_at = tweet.user.created_at)
                    
                        if(len(tweet.entities['hashtags']) == 0):
                            tweet.entities['hashtags'].append({'none': 'None'})
                        if(len(tweet.entities['urls']) == 0):
                            tweet.entities['urls'].append({'none': 'None'})
                        if(len(tweet.entities['user_mentions']) == 0):
                            tweet.entities['user_mentions'].append({'none': 'None'})
                    
                        socialContent.ent = social_Content.Entities(hashtags= tweet.entities['hashtags'], urls= tweet.entities['urls'], user_mentions = tweet.entities['user_mentions'])

                        if(tweet.place is not None):
                            socialContent.place = social_Content.Place(coordinates = tweet.place.bounding_box.coordinates, country= tweet.place.country, country_code = tweet.place.country_code , full_name = tweet.place.full_name, id_p = tweet.place.id, name = tweet.place.name, place_type = tweet.place.place_type, url= tweet.place.url)  
                        if(tweet.place is None):
                            socialContent.place = social_Content.Place(coordinates = [], country= 'None', country_code = 'None' , full_name = 'None', id_p = 'None', name = 'None', place_type = 'None', url= 'None' )  
                        
                        

                        socialContent.f_c = tweet.favorite_count
                        socialContent.retweet_count = tweet.retweet_count
                        socialContent.favorited = tweet.favorited
                        socialContent.retweeted = tweet.retweeted
                        socialContent.coordinates = tweet.coordinates
               
                        socialContent.lang = tweet.lang.encode('utf-8')
                     
                        socialContent.save()
                        print "saving tweets"
                        #all_db_id.append(tweet.id)
                        #print "ids length: "
                        #print len(all_db_id)
                except:
                    print "Some error has occured while saving this tweet"
                
                #print len(mylst)
                #del mylst[:]
                #print len(mylst)
                
                
        except:
            print "SOme Error occured while looping on tweets"