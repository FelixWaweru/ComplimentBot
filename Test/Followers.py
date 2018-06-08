import time
import tweepy
import secrets

# Authentification
CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print('Connected')

api = tweepy.API(auth)

print(api.followers_ids(screen_name="GoodFeelsBot"))

list1 = [1,2,3]
list2 = [2,3,4]
print(list(set(list1).symmetric_difference(set(list2))))