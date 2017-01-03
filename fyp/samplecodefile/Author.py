from mongoengine import *
class Author(EmbeddedDocument):
  sId  = StringField(max_length=500) #as: :source_id, type:String
  uN  = StringField(max_length=500) #as: :username, type:String
  n  = StringField(max_length=500) #as: :name, type:String
  iU  = StringField(max_length=500) #as: :image_url, type:String


  socialContent.author = Author(uN = socialProfile.n, n = socialProfile.n, sId = socialProfile.sId, iU = socialProfile.iU)