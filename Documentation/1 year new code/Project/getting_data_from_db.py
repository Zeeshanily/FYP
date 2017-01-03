import social_Content
from __inti__ import *
mongo = creatingConnection()
Connection = mongo.run()
class db_data():
    ids = []
    def get_ids_db(self):
         
         for post in  social_Content.social_content.objects:
                self.ids.append(post.id1)
         return ids
