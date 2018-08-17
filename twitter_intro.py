import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

api = twitter_api()

auth = get_auth()

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
LIV_WOE_ID = 26734
SYD_WOE_ID = 1105779

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
liv_trends = api.trends_place(LIV_WOE_ID)
syd_trends = api.trends_place(SYD_WOE_ID)

dub_trends_set = set([trend['name'] 
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name'] 
                    for trend in lon_trends[0]['trends']])

liv_trends_set = set([trend['name'] 
                    for trend in liv_trends[0]['trends']])

syd_trends_set = set([trend['name'] 
                    for trend in syd_trends[0]['trends']])

common_trends = set.intersection(syd_trends_set, liv_trends_set, lon_trends_set, dub_trends_set)

combine_trends = set.union(syd_trends_set, liv_trends_set, lon_trends_set, dub_trends_set)

different_trends = set.difference(syd_trends_set, liv_trends_set, lon_trends_set, dub_trends_set)

print(common_trends)
print(combine_trends)
print(different_trends)