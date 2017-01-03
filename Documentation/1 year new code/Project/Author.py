import datetime
from mongoengine import *
class Author(EmbeddedDocument):
        scnt = IntField(max_length = 150) #statuses_count
        fvcnt = IntField(max_length = 150) #favourites_count
        lstcnt = IntField(max_length = 150) #listed_count
        desc = StringField(max_length = 500)#description
        lct  = StringField(max_length = 100) #location
        vrf =  BooleanField()#verified
        flrcnt = IntField(max_length = 150) #followers_count
        u = StringField(max_length = 500)#url
        genb = BooleanField() #geo_enabled
        frs =BooleanField() #follow_request_sent
        frcnt = IntField(max_length = 150)#friends_count
        uid1 = IntField(max_length = 150) # Integer INT64     id
        uids = StringField(max_length = 150) # id_str
        nm = StringField(max_length = 500) #name
        snm = StringField(max_length = 500) #screen_name
        lng = StringField(max_length = 500)#lang
        tz =StringField(max_length = 500) #time_zone
        ct = DateTimeField()#created_at
       
        
