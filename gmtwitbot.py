import tweepy
import datetime

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def publictweet():
    if datetime.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday'
    if datetime.today().weekday() == 1:
        tweettopublish = 'Hey guys, Today is Tuesday.    #Tuesday'
    if datetime.today().weekday() == 2:
        tweettopublish = 'Finally Wednesday, Halfway Done.    #Wednesday'
    if datetime.today().weekday() == 3:
        tweettopublish = 'Finally, Thursday, Almost there guys!    #Thursday'
    if datetime.today().weekday() == 4:
        tweettopublish = "Thank God It's Friday.     #Friday"
    if datetime.today().weekday() == 5:
        tweettopublish = "Saturday = Good Times.   #Saturday"
    if datetime.today().weekday() == 6:
        tweettopublish = 'Sunday ready to go out!    #Sunday'

    api.update_status(tweettopublish)
    print(tweettopublish)



