import tweepy
import time

API_KEY = '**********'
API_KEY_SECRET = '**********'
ACCESS_TOKEN = '**********'
ACCESS_TOKEN_SECRET = '**********'
BEARER_TOKEN = '**********'
USER_ID = '**********'

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY,
                       consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

MENTIONIDLIST = []

def reply_to_tweet():
    mentions = client.get_users_mentions(id=USER_ID)

    for mention in mentions.data:
        if mention.id not in MENTIONIDLIST:
            print("replying to tweet...")
            MENTIONIDLIST.append(mention.id)
            response = client.create_tweet(text='REPLY TEXT', in_reply_to_tweet_id=mention.id)

while True:
    reply_to_tweet()
    time.sleep(15)
