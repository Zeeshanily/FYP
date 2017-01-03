from mongoengine import *
connect(
    #development

    # 'crm_development',
    # username='',
    # password='',
    # host='localhost', #data set after 2016
    # port=27017
    

    #production
    'heroku_7bs58nck',#heroku_fsthcm0z',
    
    username='socialcrm',#altmetrics',
    
    password='mindhacker007',#mindhacker',
    
    host='ds063725.mlab.com',
    
    port=63725#59195
    
)
# connect('activeshehri', host='ds048878.mongolab.com', port=48878)
#connect('researcher_world-dev')


