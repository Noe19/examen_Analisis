#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install tweepy


# In[10]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[11]:



###API ########################
ckey = "**********************************"
csecret = "***************************************"
atoken = "************************************************"
asecret = "***********************************j"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('*************************')  #('*******************************')
try:
    db = server.create('tra_exam')
except:
    db = server['tra_exam']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[5.9559,45.818,10.4921,47.8084])  
twitterStream.filter(track=['juegos','olimpicos'])


# In[ ]:





# In[ ]:




