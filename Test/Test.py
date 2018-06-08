import codecs
import secrets
import tweepy

CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print('Connected')


all_followers = api.followers_ids(screen_name="GoodFeelsBot")
with open('test.txt', 'r') as textCheck1:
    followers_list = textCheck1.read().splitlines()
    print(followers_list)
    # if all_followers not in followers_list:
    #
    #
    # elif all_followers in followers_list:
    #     break
def replier():
    reply = "Hi"

    #reply to statuses directed towards the bot

    replyTwt = api.search(q="@GoodFeelsBot", count=100)
    for tweet in replyTwt:
        repId = tweet.id
        with open('test.txt', 'r') as textCheck2:
            line = textCheck2.read().splitlines()
            unreplied = list(set(str(repId)).symmetric_difference(set(line)))
            print(len(unreplied))
            print(len(line))
            print(repId)

            if (len(unreplied)) == 0:
                break
            else:
                loop = len(unreplied)
                i = 0
                while i < loop:
                    print("Reply sent")
                    sentreply = open('test.txt', 'w')
                    sentreply.writelines(unreplied[i])
                    checker2 = open('test.txt', 'r')
                    checkerList = sentreply.read().splitlines()
                    checker = list(set(str(repId)).symmetric_difference(set(checkerList)))
                    if (len(unreplied)) == 0:
                        break
                    else:
                        i = i+1



            # if str(repId) in line:
            #     break
            #
            # elif str(repId) not in line:
            #     print("Reply received.")
            #     words = tweet.text
            #     print(words)
            #     sn = tweet.user.screen_name
            #     str(sn)
            #     m = "@" + sn + " Heyhey. " + reply + " :) @" + sn
            #     api.update_status(m, tweet.id)
            #     print("Reply Sent")
            #     with codecs.open('/home/MeanBot001/ComplimentBot/Replies.txt', 'w') as followerText:
            #         followerText.writelines(str(repId) + "\n")
            # break
