from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textwrap import TextWrapper
import json

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_data(self, stream):
        data = json.loads(stream);
        new_dic = {};
        new_dic["name"] = data["user"]["screen_name"];
        new_dic["tweet"] = data["text"];
        new_dic["time"] = data["user"]["created_at"];
    
        with open('tweets.json', 'a') as outfile:
            json.dump(new_dic, outfile, indent = 4)

    def on_status(self, data):
        try:
            
            print "Tweet added";
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            print "Somethings gone wrong.";
            print data;
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
