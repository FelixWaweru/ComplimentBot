import random
import threading

import tweepy, time, secrets

# Authentification
CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print('Connected')



def deleter():
    try:
        for status in api.user_timeline():
            print("Deleting tweet.\n")
            status_id = status.id
            api.destroy_status(status_id)
            print("Tweets deleted.\n")
            break
    except:
        print("Tweet could not be deleted. Pls try again later.\n")

def startDeletion():
    loops = input("How many tweets you want gone? \n")
    i = 0
    while i is not int(loops):
        deleter()
        i = i + 1
    else:
        print("Deletion completed.")

