import random
import tweepy

auth = tweepy.0AuthHandler("accesskeys","secretkey")
auth.set_access_token(,)
api = tweepy.API(auth)

def memify(text):
    new = []
    b = '..... ok boomer'
    for i in range(len(text)-len(b)):
        c = text[i]
        r = random.randint(0,1)
        if r:
            new.append(c.upper())
        else:
            new.append(c.lower())
    return ''.join(new + [b])
       
tweets = api.user_timeline(screen_name="kanyewest")
for tweet in tweets:
    if tweet.text[0:2] != "RT":
        api.update_with_media('cat.jpg', '@kanye {}'.format(memify(tweet.txt)), first_tweet.id)
