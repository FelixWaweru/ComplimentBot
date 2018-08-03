import codecs
import secrets
import tweepy
import random
import re

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


# prefixrandomizer = random.randint(0, 10)
# complimentsrandomizer = random.randint(0, 34)
# emojirandomizer = random.randint(0, 27)
# update = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]
#
# prefixrandomizer = random.randint(0, 10)
# complimentsrandomizer = random.randint(0, 34)
# emojirandomizer = random.randint(0, 27)
# update2 = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " : " + emojis[emojirandomizer]

# i = 0
# while i is not 12:
#     print(prefix[i])
#     i = i+1


# Used to randomize the generated tweets
def tweet_randomizer():
    prefixrandomizer = random.randint(0, (len(prefix)-1))
    complimentsrandomizer = random.randint(0, (len(compliments)-1))
    emojirandomizer = random.randint(0, (len(emojis)-1))
    update = prefix[prefixrandomizer] + " you are " + compliments[complimentsrandomizer] + " " + emojis[
        emojirandomizer]
    tweet_randomizer.latest_tweet = update
    return update

# TODO: Look into automatically following everyone who likes the tweets
# class replyStreamer(tweepy.StreamListener):
#     # Method carried out when tweet is received
#     def on_event(self, status):
#         print(status.event)
#
#         if stream.event is 'favourite':
#             print("True dat")
#
#         else:
#             print('False')
        # if status.event == 'favorite':
        #     print("Someone liked your post!")
        #     if api.exists_friendship("@GoodFeelsBot", sn) is False:
        #         try:
        #             api.create_friendship(sn)
        #             print("Now following " + sn + "\n")
        #         except tweepy.error.TweepError:
        #             print("Could not follow.")
        #     else:
        #         print("You already follow " + sn)

# while i is not 10:
#     rep = Replier()
#     randomizer()
#     i = i + 1

# tweet = tweet_randomizer()
# while i is not 10:
#     while running is True:
#         try:
#             print(tweet_randomizer())
#             print("First try Tweet \n")
#             break
#
#         except tweepy.error.TweepError:
#             print(tweet)
#             print("Second try Tweet \n")
#             break
# def on_status():
#     new_followers = api.followers()
#     for i in new_followers:
#         sn = i.screen_name
#         str(sn)
#         m = "@" + sn + " Hello " + "@" + sn + " . " + tweet_randomizer() + "\n I hope you have a great day today :)"
#         print(m)
#
#
# on_status()
# def stream():
#     ReplyStreamer = replyStreamer()
#     myStream = tweepy.Stream(auth=api.auth, listener=ReplyStreamer)
#     myStream.userstream()
#
#
# stream()
# print(api.followers('GoodFeelsBot'))
# for user in api.followers('GoodFeelsBot'):
#     print(user.screen_name)
followers = api.lookup_friendships('GoodFeelsBot','WeruFe')
followers2 = api.followers_ids('WeruFe')

print(followers2)
for id in followers2:
    api.create_friendship(id)
    print("Followed")

# def get_user_ids_of_post_likes(post_id):
#     try:
#         json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
#         found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
#         unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
#         return unique_ids
#     except urllib2.HTTPError:
#         return False
#
# # Example:
# # https://twitter.com/golan/status/731770343052972032
#
# print (get_user_ids_of_post_likes(731770343052972032))