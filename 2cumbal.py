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
ckey = "emWGybRsX7nicbOuYQkwEiQfR"
csecret = "8xETeMIhFutrBT0TCC4vB7D5ZDrbZ8eLdTJDcje4Hp3hiPSi5X"
atoken = "1415800172152561668-IVf8r6I342niwblUW38HnLLIXjSX8A"
asecret = "OL2f8rlNQM8ETLJxWQHPo8m04cgiKSsylwfI90ytPsW4j"
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
server = couchdb.Server('http://CUMBAL:12345@127.0.0.1:5984')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tra_exam')
except:
    db = server['tra_exam']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[5.9559,45.818,10.4921,47.8084])  
twitterStream.filter(track=['juegos','olimpicos'])


# In[ ]:





# In[ ]:




