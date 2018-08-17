import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

api = twitter_api()

auth = get_auth()

count = 10
query = 'Skerries'

#Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print(json.dumps(result._json, indent=2))
    
for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.followers_count)
    print(status.place)