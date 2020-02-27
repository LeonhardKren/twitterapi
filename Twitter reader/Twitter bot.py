from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStreamer():
    """
    Class for streaming and processing live tweets
    """
    def __innit__(self):
        pass

    def stream_tweets(self, fetched_tweet_filename, hash_tag_list, Places_list):
        #This handles twitter authentication and the connection to the twitter streaming api
        listener = TwitterListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET_KEY)
        auth.set_access_token(twitter_credentials.ACCES_TOKEN, twitter_credentials.ACCES_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)
        stream.filter(locations=Places_list)

class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    hash_tag_list = ["donald trump"]
    fetched_tweets_filename = "tweets.txt"
    Places_list = ["Washington, Detroit, Houston"]
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list, Places_list)
