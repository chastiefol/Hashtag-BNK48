# Import modules
import tweepy
import json
import csv

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        """ Import streaming text to CSV """
        with open('bnkdata.csv', 'a', encoding='utf-8',  newline='') as writeFile:
            payload = [tweet.created_at, tweet.text.replace('\n', ' ')]
            writer = csv.writer(writeFile)
            writer.writerow(payload)
            print(sum(1 for line in csv.reader( open('bnkdata.csv', 'r', encoding='utf-8'))))

def main ():
    """ Create credential variables"""
    consumer_key = 'your_consumer_key'        # put your consumer_key from Twitter API
    consumer_secret = 'your_consumer_secret'  # put your consumer_secret from Twitter API
    access_token = 'your_access_token'        # put your access_token from Twitter API
    access_secret = 'your_access_secret'      # put your access_secret from Twitter API

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(track=['#BNK48'])

main()
