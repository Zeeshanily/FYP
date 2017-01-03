import datetime
from mongoengine import *
class Entities(EmbeddedDocument):
    hstg = ListField(DictField()) #hashtags
    ur =  ListField(DictField())   #urls
    usrmn = ListField(DictField()) #user_mentions
   # meta = { "collection":"social_contents",'strict': False}

