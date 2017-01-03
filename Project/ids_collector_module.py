import time
import tweepy 

class ids_collector():
    def collector(self, array, api):
        ids = []
        try:
            for i in array:
                user_timeline = api.user_timeline(screen_name=i ,count=1)
                print len(user_timeline)
                ids.append(user_timeline[0].id_str)
                print ids
                print i
                time.sleep(60)
            return ids
        except:
            print "Error came here wait for 15 minutes now"
            

