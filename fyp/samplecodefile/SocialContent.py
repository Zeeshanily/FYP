from SocialProfile import SocialProfile
from customRefs.Author import *
import datetime

class SocialContent(Document):
	sId = StringField(max_length=500) #   source_id,           type:String
	h   = StringField(max_length=500) #     host,                type:String
	sCT = StringField(max_length=500) #   source_content_type, type:String
	t   = StringField(max_length=4500) #     text,                type:String
	u   = StringField(max_length=500) #     url,                 type:String
	lD  = DateTimeField(default=datetime.datetime.now) #    load_date,           type:Time
	cD 	= DateTimeField(default=datetime.datetime.now) #    create_date,         type:Time
	uD 	= DateTimeField(default=datetime.datetime.now) #    update_date,         type:Time
	pSId = StringField(max_length=500) #  parent_source_id,    type:String
	rcps = ListField(StringField(max_length=150)) #  recipients,          type:Array,  default: []
	# a    = ReferenceField(SocialProfile) #     author,              type:SocialProfileRef
	fS =  StringField(max_length=500) #    fetch_source,        type:String
	author = EmbeddedDocumentField(Author)
	cA = MapField(field=StringField()) #    content_attributes,           type:Hash
	cls = MapField(field=StringField())  #   classifications,              type:Hash
	clsA = ListField(StringField(max_length=200), default=[]) #  classifications_array,        type:Array
	clI = ListField(StringField(max_length=200)) #   classification_index,         type:Array
	clA = MapField(field=StringField()) #   classification_attributes,    type:Hash
	social_profile_id = ObjectIdField() # social_profile_id, type:ObjectId
	meta = { "collection":"social_contents",'strict': False}
	se = StringField(max_length=500) #sentiment
