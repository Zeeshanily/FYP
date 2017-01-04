import datetime
from mongoengine import *
class Entities(EmbeddedDocument):
    hashtags = ListField(DictField()) #hashtags
    urls =  ListField(DictField())   #urls
    user_mentions = ListField(DictField()) #user_mentions
   # meta = { "collection":"social_contents",'strict': False}


