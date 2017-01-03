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
                count1 = social_Content.social_content.objects(id1=tweet.id).count()
                print count1
                if ( count1 >= 1):
                    print "Already exist"
                else:
                    socialContent = social_Content.social_content()
                    socialContent.c_at = tweet.created_at
                    socialContent.id1 = tweet.id
                    socialContent.id_s = tweet.id_str.encode('utf-8')
                    socialContent.text = tweet.text.encode('utf-8')
                    socialContent.src = tweet.source.encode('utf-8')
                    socialContent.i_r_t_s_i = tweet.in_reply_to_status_id
                    socialContent.i_r_t_s_i_s = tweet.in_reply_to_status_id_str
                    socialContent.i_r_t_u_i = tweet.in_reply_to_user_id
                    socialContent.i_r_t_u_i_s = tweet.in_reply_to_user_id_str
                    socialContent.i_r_t_s_n = tweet.in_reply_to_screen_name
                    socialContent.general_tags = tag_tweet
                    socialContent.author = social_Content.Author(scnt= tweet.user.statuses_count, fvcnt= tweet.user.favourites_count, lstcnt = tweet.user.listed_count, desc = tweet.user.description, lct =  tweet.user.location, vrf = tweet.user.verified, flrcnt = tweet.user.followers_count, u = tweet.user.url, genb= tweet.user.geo_enabled, frs= tweet.user.follow_request_sent, frcnt = tweet.user.friends_count, uid1 =  tweet.user.id , uids = tweet.user.id_str, nm = tweet.user.name, snm = tweet.user.screen_name, lng = tweet.user.lang, tz = tweet.user.time_zone, ct = tweet.user.created_at)
                
                    if(len(tweet.entities['hashtags']) == 0):
                        tweet.entities['hashtags'].append({'none': 'None'})
                    if(len(tweet.entities['urls']) == 0):
                        tweet.entities['urls'].append({'none': 'None'})
                    if(len(tweet.entities['user_mentions']) == 0):
                        tweet.entities['user_mentions'].append({'none': 'None'})
                
                    socialContent.ent = social_Content.Entities(hstg= tweet.entities['hashtags'], ur= tweet.entities['urls'], usrmn = tweet.entities['user_mentions'])           
                    socialContent.r_c = tweet.retweet_count
                    socialContent.f_c = tweet.favorite_count
            
                    socialContent.fvrt = tweet.favorited
                    socialContent.rtw = tweet.retweeted
           
                    socialContent.lang = tweet.lang.encode('utf-8')
                 
                    socialContent.save()
                    print "saving tweets"
                    #all_db_id.append(tweet.id)
                    #print "ids length: "
                    #print len(all_db_id)
            
            
            #print len(mylst)
            #del mylst[:]
            #print len(mylst)
                
                
        except:
            print "SOme Error occured while saving tweets"