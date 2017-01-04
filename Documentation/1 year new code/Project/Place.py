from mongoengine import *
class Place(EmbeddedDocument):
    coordinates = ListField() #bounding_box
    country =  StringField(max_length = 150)   
    country_code = StringField(max_length = 150)  
    full_name = StringField(max_length = 150) 
    id_p = StringField(max_length=500) #place id
    name = StringField(max_length = 500) 
    place_type = StringField(max_length=500) 
    url = StringField(max_length = 500) # url