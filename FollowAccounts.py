# import statements

# -*- coding: utf-8 -*-
#!/usr/bin/python3.6
import codecs
import random
import threading
import sys
import tweepy, time, secrets

# Authentification
CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
print('Connected')


# Function used to follow a specific persons' followers
def follow(userName):
    try:
        followers2 = api.followers_ids(userName)
        skip = False
        i = 0
        for id in followers2:
            try:
                api.create_friendship(id)
                print("Followed")
            except tweepy.error.TweepError:
                error = str(tweepy.error.TweepError)
                print('Error. Skipping user follow \n')
                i = 1
                if i is 1:
                    skip = True
                    continue
                if skip:
                    i = 0
                    skip = False
                    continue

    except:
        print("Please enter a valid username pls")

