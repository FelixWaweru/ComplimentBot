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

# Prefixes that are appended to the beginning of the tweets
prefix = ["I hope you know that",
          "Remember,",
          "Remind yourself,",
          "Remember that",
          "Please remember,",
          "Kindly remind yourself that",
          "Kindly remind yourself,",
          "Appreciate yourself,",
          "Take it easy today,",
          "Take a break and know that",
          "Somebody would want you to know that",
          "You are cared for and",
          "Forget your worries,",
          "Hello there,",
          "Recognize that",
          "Bear in mind,",
          "Please know that",
          "Do know that",
          "Know that",
          "Be conscious of the fact that",
          "Be aware of the fact that",
          "Realize that",
          "Please remember,",
          "Hey,",
          "Keep in mind that",
          "Remind yourself that",
          "Take some time today to remember that",
          "It's a fact that"]

# Compliments that are appended to the middle of the tweets
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
               "lovely.",
               "breathtaking.",
               "unique.",
               "truly wonderful.",
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

# Emojis that are appended to the end of the tweets
emojis = ["❤️", "♥️", "💗", "💓", "💕", "💖", "💞 " "💘", "💛", "💙", "💜", "💚", "💝", "💌", "🌝", "🌞", "☀️", "🌸",
          "🌹", "🌺", "🌻", "💐", "🌼", "🏵️", "⭐", "🌟", "🌠", "🌈"]


# Used to randomize the generated tweets
def tweet_randomizer():
    prefixrandomizer = random.randint(0, (len(prefix)-1))
    complimentsrandomizer = random.randint(0, (len(compliments)-1))
    emojirandomizer = random.randint(0, (len(emojis)-1))
    update = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + "  " + emojis[
        emojirandomizer]
    tweet_randomizer.latest_tweet = update
    return update


# Class used to generate a persistent connection to the bot Replies
class replyStreamer(tweepy.StreamListener):
    # Method carried out when tweet is received
    def on_status(self, status):
        sn = status.user.screen_name
        print("\n Reply received from " + sn + "\n")
        print(status.text)
        str(sn)
        m = "@" + sn + " Hello " + "@" + sn + " . " + tweet_randomizer() + "\n I hope you have a great day today :)"
        api.create_favorite(status.id)
        api.update_status(m, status.id)
        print("\n Reply Sent at " + time.strftime("%Y-%m-%d %H:%M") + "\n")
        print("Tweet: " + m + "\n")




def tweeter():
    while running is True:
        try:
            api.update_status(tweet_randomizer())
            print("\n ✓ Tweet Sent at \n")
            print (time.strftime("%Y-%m-%d %H:%M") + "\n")
            print("Countdown to next Tweet \n")
            for i in range(240, 0, -10):
                time.sleep(600)
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()

        except tweepy.error.TweepError:
            # Delete and resend new tweet.
            for status in api.user_timeline():
                if status.text == tweet_randomizer.latest_tweet:
                    print("\n ✓ Deleting already sent tweet \n")
                    status_id = status.id
                    api.destroy_status(status_id)
                    api.update_status(tweet_randomizer())
                    print("\n ✓ Tweet Resent at \n")
                    print(time.strftime("%Y-%m-%d %H:%M") + "\n")
                    print("Countdown to next Tweet \n")
                    for i in range(240, 0, -10):
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


# Method used to send a direct message to every user
def direct_messenger():
    allFollowers = api.followers()
    message = input("Please type in your bulk message: \n")
    for i in allFollowers:
        api.send_direct_message(user_id=i.id,
                                text="Heyhey @" + i.screen_name + " . " + message)
        print("You messaged @" + i.screen_name)

def exitBot():
    sys.exit(0)


# Main method used to run all the bot functions in a thread
def threader():
    tweeterThread = threading.Thread(target=tweeter)
    # followerThread = threading.Thread(target=new_follower)
    replierThread = threading.Thread(target=replier)

    tweeterThread.start()
    # followerThread.start()
    replierThread.start()


