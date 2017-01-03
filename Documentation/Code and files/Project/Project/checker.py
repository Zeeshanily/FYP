from mongoengine import connect
connect('project1')
import datetime
from mongoengine import *
from Author import *
#from Entities import *
import datetime

class Entities(EmbeddedDocument):
    hstg = ListField(StringField(max_length=150)) #hashtags
    ur =  ListField(StringField(max_length=150))   #urls
    usrmn = ListField(StringField(max_length=150)) #user_mentions
   # meta = { "collection":"social_contents",'strict': False}


class social_content(Document):
    c_at = DateTimeField() # created_at  default=datetime.datetime.now
    id1 = IntField(max_length = 150, unique = True) # Integer INT64
    id_s = StringField(max_length = 150) # id_str
    text = StringField(max_length=500)
    src = StringField(max_length = 500) # source
    i_r_t_s_i = IntField(max_length = 150) # in_reply_to_status_id
    i_r_t_s_i_s = StringField(max_length=500) # in_reply_to_status_id_str
    i_r_t_u_i = IntField(max_length = 150) # in_reply_to_user_id
    i_r_t_u_i_s = StringField(max_length=500) # in_reply_to_user_id_str
    i_r_t_s_n = StringField(max_length=500) # in_reply_to_screen_name

    author = EmbeddedDocumentField(Author)
    r_c = IntField(max_length = 150) # retweet_count
    f_c = IntField(max_length = 150) # favorite_count
   # ent = EmbeddedDocumentField(Entities) # entities
    fvrt = BooleanField() # favorited
    rtw = BooleanField() # retweeted
  
    lang = StringField(max_length=500)
 
    meta = { "collection":"social_contents",'strict': False}
   # author = StringField(max_length = 50)
    #place

        
#import social_Content
print social_content.objects.id1
