# import statements
import random

import tweepy,os.path, time, secrets

# Authentification
from twitter import stream

CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print('Connected')
tweets = ["You are unloved.", "Sometimes if you squint really hard you can see your future crumbling around you as time "
          "goes on.", "Today is the day you finally acheive something great, seeing this tweet.",
          "I fart in your general direction.", "Someone laughed at you today and you will never know what it was about."
    ,"Though they may never admit it, your parents sometimes dislike you strongly.", "I have good and bad news. Good "
    "news,someday you will die, bad news, we have to attend your funeral.", "Nobody likes poop and yet they made an "
    "emoji after it. You are emojiless and thus hated more than poop.", "You are your own worst enemy and everything "
    "you think is wrong with you is who you really are.", "You are kinda smelly."]
rep = "I am a bot incapable of emotion or responsiveness. Go away."
def tweeter():
    try:
        randomizer = random.randint(0, 9)
        response = tweets[randomizer]
        status = api.update_status(response)
        print("Tweet Sent")
        time.sleep(21600)
    except:
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                status_id = status.id
                api.destroy_status(status_id)
                api.update_status(response)
                print("Tweet Sent")
                break
            except:
                pass

def replier():
    #reply to statuses directed towards the bot
    twt = api.search(q="MeanBot001")
    t = ['meanbot001', 'Meanbot001', 'meanBot001']
    for s in twt:
        for i in t:
            if i == s.text:
                print("Reply received")
                sn = s.user.screen_name
                m = "@%s " + rep % (sn)
                s = api.update_status(m, s.id)
                print("Reply Sent")

def messager():
    #reply to DM's directed towards the bot
    direct_message = api.direct_messages()
    for dm in direct_message:
        dm_id= dm.id
        api.send_direct_message(dm_id, rep)
        print("Dm Sent")

def new_follower():
    new_followers = api.followers()
    for i in new_followers:
        api.send_direct_message(user_id=i.from_user, text="Please do not take any personal offence from any of my tweets.")
        print("You messaged new user " + i.from_user)

running = True
while running is True:
    tweeter()
    replier()
    messager()
    new_follower()