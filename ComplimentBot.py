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

running = True

prefix = ["I hope you know that",
          "Remember that",
          "Please know that",
          "Do know that",
          "You,",
          "Know that",
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
               "allowed to feel great about yourself today.",
               "the most wonderful and amazing you you can be.",
               "the universe incarnate. Incomprehensibly spectacular and unique.",
               "making someone out there very proud.",
               "worth the life you have been gifted.",
               "deserving of all the love in the world.",
               "looking lovely today.",
               "talented.",
               "so special.",
               "beautiful.",
               "one of a kind.",
               "capable of anything you put your mind to.",
               "a joy",
               "a valuable human being.",
               "secretly an inspiration to many people around you.",
               "a pleasure to know.",
               "worth the life you have been gifted.",
               "even more beautiful on the inside than you are on the outside.",
               "a great example to others.",
               "a good friend.",
               "the change this world needs.",
               "amazing!",
               "valued.",
               "enough.",
               "really something special."
               ]

emojis = ["❤️", "♥️", "💗", "💓", "💕", "💖", "💞 " "💘", "💛", "💙", "💜", "💚", "💝", "💌", "🌝", "🌞", "☀️", "🌸",
          "🌹", "🌺", "🌻", "💐", "🌼", "🏵️", "⭐", "🌟", "🌠", "🌈"]

prefixrandomizer = random.randint(0, 11)
complimentsrandomizer = random.randint(0, 34)
emojirandomizer = random.randint(0, 27)
update = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]

prefixrandomizer = random.randint(0, 11)
complimentsrandomizer = random.randint(0, 34)
emojirandomizer = random.randint(0, 27)
update2 = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]

allstatus = [update, update2]
statusrandomizer = random.randint(0, 1)
# allupdates = allstatus[statusrandomizer]
allupdates = allstatus[statusrandomizer]

class replyStreamer(tweepy.StreamListener):
    # Method carried out when tweet is received
    def on_status(self, status):
        prefixrandomizer2 = random.randint(0, 11)
        complimentsrandomizer2 = random.randint(0, 34)
        emojirandomizer2 = random.randint(0, 27)
        reply = prefix[prefixrandomizer2] + " you are " + compliments[complimentsrandomizer2] + " : " \
                + emojis[emojirandomizer2]
        print("Reply received.")
        print(status.text)
        sn = status.user.screen_name
        str(sn)
        m = "@" + sn + " Heyhey. " + reply + " :) @" + sn
        api.create_favorite(status.id)
        api.update_status(m, status.id)
        print("Reply Sent")


def tweeter():
    while running is True:
        try:
            api.update_status(update)
            print("Tweet Sent \n")
            print("Countdown to next Tweet \n")
            for i in range(120, 0, -10):
                time.sleep(600)
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()

        except tweepy.error.TweepError:
            api.update_status(update2)
            print("Tweet Resent \n")
            print("Countdown to next Tweet \n")
            for i in range(120, 0, -10):
                time.sleep(600)
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()
                break



def replier():
    #reply to statuses directed towards the bot
    ReplyStreamer = replyStreamer()
    myStream = tweepy.Stream(auth=api.auth, listener=ReplyStreamer)

    replyTwt = myStream.filter(track=['@GoodFeelsBot'], async=True)

# def new_follower():
#     new_followers = api.followers()
#     for follower in new_followers:
#         with open('/home/MeanBot001/ComplimentBot/Followers.txt', 'r') as textCheck1:
#             followerId = follower.id
#             str(followerId)
#             followerLine = textCheck1.readlines()
#             if str(followerId) in followerLine:
#                     break
#             elif str(followerId) not in followerLine:
#                 with codecs.open('/home/MeanBot001/ComplimentBot/Followers.txt', 'w') as followerText:
#                     for i in new_followers:
#                         api.send_direct_message(user_id=i.id,
#                                             text="Heyhey @" + i.screen_name + ". Stick around for some daily positivity or mention me "
#                                                                               "anywhere on Twitter and I'll bring the positivity to you :)")
#                         print("You messaged new user @" + i.screen_name)
#                         followerText.writelines(str(followerId) + "\n")
#             break

def directMessenger():
    allFollowers = api.followers()
    message = input("Please type in your bulk message: \n")
    for i in allFollowers:
        api.send_direct_message(user_id=i.id,
                                text="Heyhey @" + i.screen_name + " . " + message)
        print("You messaged @" + i.screen_name)

def exitBot():
    sys.exit(0)

def threader():
    tweeterThread = threading.Thread(target=tweeter)
    # followerThread = threading.Thread(target=new_follower)
    replierThread = threading.Thread(target=replier)

    tweeterThread.start()
    # followerThread.start()
    replierThread.start()


