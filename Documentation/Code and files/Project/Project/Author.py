import datetime
from mongoengine import *
class Author(EmbeddedDocument):
        statuses_count = IntField(max_length = 150) #statuses_count
        favourites_count = IntField(max_length = 150) #favourites_count
        listed_count = IntField(max_length = 150) #listed_count
        description = StringField(max_length = 500)#description
        location  = StringField(max_length = 100) #location
        verified =  BooleanField()#verified
        followers_count = IntField(max_length = 150) #followers_count
        url = StringField(max_length = 500)#url
        geo_enabled = BooleanField() #geo_enabled
        profile_image_url = StringField(max_length = 500)

        frs =BooleanField() #follow_request_sent
        frcnt = IntField(max_length = 150)#friends_count
        uid1 = IntField(max_length = 150) # Integer INT64     id

        id_str = StringField(max_length = 150) # id_str
        name = StringField(max_length = 500) #name
        screen_name = StringField(max_length = 500) #screen_name
        lang = StringField(max_length = 500)#lang
        time_zone =StringField(max_length = 500) #time_zone
        created_at = DateTimeField()#created_at
       
        
