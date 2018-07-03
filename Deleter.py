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


# function used to delete the tweet
def deleter():
    try:
        for status in api.user_timeline():
            print("Deleting tweet.\n")
            status_id = status.id
            status_text = status.text
            api.destroy_status(status_id)
            print("Deleted " + status_text + "\n")
            break
    except:
        print("Tweet could not be deleted. Pls try again later.\n")


# function used to loop through the deleter() function for a specified number of times
def startDeletion():
    loops = input("\n How many tweets you want gone? \n")
    i = 0
    while i is not int(loops):
        deleter()
        i = i + 1
    else:
        print("Deletion completed.")

