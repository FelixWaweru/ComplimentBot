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
api = tweepy.API(auth)
print('Connected')
prefix = ["I hope you know that",
          "Remember that",
          "Please know that",
          "Do know that",
          "You,",
          "Please remember,",
          "Hey there,",
          "Keep in mind that",
          "Remind yourself that",
          "Take some time today to remember that",
          "It's a fact that"]

compliments = ["an amazing person.",
               "loved.",
               "made of star dust and love.",
               "capable of anything you set your heart to.",
               "the world to someone.",
               "doing great so far even if you don't feel like it yet.",
               "not alone. You have us here with you.",
               "going to make it through the day.",
               "looking great today.",
               "slaying so hard right now. Almost called the murder detectives on you.",
               "allowed to feel great about yourself.",
               "the most wonderful and amazing you you can be.",
               "the universe incarnate. Incomprehensibly spectacular and unique.",
               "making someone out there very proud.",
               "worth the life you have been gifted.",
               "deserving of all the love in the world.",
               "looking lovely today.",
               "secretly an inspiration to many people around you."
               ]

emojis = ["❤", "♥", "💗", "💓", "💕", "💖", "💞 " "💘", "💛", "💙", "💜", "💚", "💝", "💌", "🌝", "🌞", "☀"]

prefixrandomizer = random.randint(0, 10)
complimentsrandomizer = random.randint(0, 17)
emojirandomizer = random.randint(0, 16)
update = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]

statements = ["I think you're cool",
              "Your smile is the highlight of any day.",
              "If I was alive, I'd want to be your friend.",
              "Are you a banana skin because I find you a-peeling.",
              "You must smell amazing."
              ]
prefixrandomizer = random.randint(0, 10)
complimentsrandomizer = random.randint(0, 17)
emojirandomizer = random.randint(0, 16)
update2 = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]

allstatus = [update, update2]
statusrandomizer = random.randint(0, 1)
# allupdates = allstatus[statusrandomizer]
allupdates = update

def tweeter():
    try:
        api.update_status(allupdates)
        print("Tweet Sent")
        time.sleep(7200)
    except tweepy.error.TweepError:
        for status in api.user_timeline():
            if status == allupdates:
                print("Uh oh. Deleting already sent tweet")
                status_id = status.id
                api.destroy_status(status_id)
                api.update_status(allupdates)
                print("Tweet Resent")
                time.sleep(7200)
                break

def replier():
    prefixrandomizer2 = random.randint(0, 10)
    complimentsrandomizer2 = random.randint(0, 17)
    emojirandomizer2 = random.randint(0, 16)
    reply = prefix[prefixrandomizer2] + " you are " + compliments[complimentsrandomizer2] + " : " + emojis[emojirandomizer2]
    #reply to statuses directed towards the bot
    repIds = []
    twt = api.search(q="@GoodFeelsBot", count=100)
    for tweet in twt:
        with open('Replies.txt') as textCheck2:
            repId = tweet.id
            str(repId)
            found = False
            for line in textCheck2:
                if str(repId) in line:  # Key line: check if `w` is in the line.
                    pass
                    found = True
            if not found:
                print("Reply received.")
                word = tweet.text
                print(word)
                sn = tweet.user.screen_name
                str(sn)
                m = "@" + sn + " Heyhey. " + reply + " :) @" + sn
                api.update_status(m, tweet.id)
                print("Reply Sent")
                with codecs.open('/home/MeanBot001/ComplimentBot/Replies.txt', 'w') as followerText:
                    followerText = open('Replies.txt', 'w')
                    followerText.writelines(str(repId) + "\n")
                    repIds.append(repId)
            break
    time.sleep(180)

def new_follower():
    new_followers = api.followers()
    for follower in new_followers:
        with open('Followers.txt') as textCheck1:
            repId = follower.id
            str(repId)
            found = False
            for line in textCheck1:
                if str(repId) in line:  # Key line: check if `w` is in the line.
                    pass
                    found = True
            if not found:
                with codecs.open('/home/MeanBot001/ComplimentBot/Followers.txt', 'w') as followerText:
                    for i in new_followers:
                        api.send_direct_message(user_id=i.id,
                                            text="Heyhey @" + i.screen_name + ". Stick around for some daily positivity or mention me "
                                                                              "anywhere on Twitter and I'll bring the positivity to you :)")
                        print("You messaged new user @" + i.screen_name)
                        followerText.writelines(str(repId) + "\n")
            break

running = True
while running is True:
    t = threading.Thread(target=tweeter)
    t.start()
    t1 = threading.Thread(target=new_follower)
    t1.start()
    replier()
    exitCode = input("Type exit to end process")
    if exitCode is "exit":
        sys.exit("Exiting")