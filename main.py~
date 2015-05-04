#Main for twitter streamer

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textwrap import TextWrapper
import json
import StdOutListenerClass

save_file = open('tweets.json', 'a')

searchTerm = "#starwars" #insert your own stuff here!

access_token = "INSERT OWN CODE HERE"
access_token_secret = "INSERT OWN CODE HERE"
consumer_key = "INSERT OWN CODE HERE"
consumer_secret = "INSERT OWN CODE HERE"
         
if __name__ == '__main__':
    listener = StdOutListenerClass.StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    stream = Stream(auth, listener);
    stream.filter(track=[searchTerm]);
    
    
    

        
