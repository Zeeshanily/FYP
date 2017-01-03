import time
import tweepy 

class ids_collector():
    def collector(self, data, api):
        ids = []
        user_timeline = []
        try:
            for i in range(0,len(data)-1):
                try:
                    
                    user_timeline = api.user_timeline(screen_name=data[i] ,count=1)
                    print len(user_timeline)
                    ids.append(user_timeline[0].id_str) # only first tweet's id
                    print ids
                    print data[i]
                    time.sleep(60)
            

                except:
                    print "Error came here wait for 15 minutes now"
                    ids.append(user_timeline[0].id_str)
                    time.sleep(900)
            return ids
        except:
                return ids
                print "reuturning back due to some error"

