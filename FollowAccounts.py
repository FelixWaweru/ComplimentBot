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

        # Function used to loop through a specific number of followers
        times = 0
        loops = input("How many accounts do you wish to follow? ")
        while times is not int(loops):
            for id in followers2:
                try:
                    status = api.show_friendship("@GoodFeelsBot", target_id=id)
                    if status[0].following is False:
                        api.create_friendship(id)
                        print((times+1) + "Followed " + str(id))
                        del followers2[0]
                        time.sleep(300)
                        break
                    else:
                        print((times+1) + "Already Following " + str(id))
                        del followers2[0]
                        break

                except tweepy.error.TweepError:
                    print('\n Error. Skipping user follow \n')
                    i = 1
                    if i is 1:
                        skip = True
                        continue
                    if skip:
                        i = 0
                        skip = False
                        continue
            times = times + 1
    except Exception as e:
        print('Kindly try again. Error: '+ str(e))

