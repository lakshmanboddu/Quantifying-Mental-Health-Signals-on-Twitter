
# coding: utf-8

# In[12]:


import tweepy
import csv
import re

# Consumer keys and access tokens, used for OAuth
consumer_key = 'jxpGx90bgjqZDiRcdiT2uLUO9'
consumer_secret = 'DPI1QRcRE5CP37IaLDxJpRT0s3k0Dv1H2alhHWlPwCnt5PW81n'
access_token = '1396904694-SHm12SMxHJwhKT7fB5ivv0P9IHvZIC753wDMWT5'
access_token_secret = 'ejVaIC7oMmfyUiT6gYwlOUp6VpoFeMjkB3f5MviT0z0Sx'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
# Open/Create a file to append data
with open("test.csv",'w') as f:
    writer = csv.writer(f, dialect='excel')

usernames = ['zangerdanger',
             'R2D1ck2',
             'AIIStarBacon',
             'Kyashi_Cosplay',
             'Froymyjoy',
             'aloofloofah',
             'bethwithanf_',
             'JWebbConsulting',
             'toxidlotus',
             'Sandford_Police',
             'xo_roni_yt',
             'saveyoursellf']
alltweet =[]
for status in tweepy.Cursor(api.user_timeline, screen_name="zangerdanger", tweet_mode='extended').items(200):
    if not status.retweeted and 'RT @' not in status._json['full_text']:
        alltweet.append(status._json['full_text'])

for status in tweepy.Cursor(api.user_timeline, screen_name="Kyashi_Cosplay", tweet_mode='extended').items(100):
    if not status.retweeted and 'RT @' not in status._json['full_text']:
        alltweet.append(status._json['full_text'])


for status in tweepy.Cursor(api.user_timeline, screen_name="JWebbConsulting", tweet_mode='extended').items(200):
    if not status.retweeted and 'RT @' not in status._json['full_text']:
        alltweet.append(status._json['full_text'])

for status in tweepy.Cursor(api.user_timeline, screen_name="Sandford_Police", tweet_mode='extended').items(100):
    if not status.retweeted and 'RT @' not in status._json['full_text']:
        alltweet.append(status._json['full_text'])

for status in tweepy.Cursor(api.user_timeline, screen_name="saveyoursellf", tweet_mode='extended').items(100):
    if not status.retweeted and 'RT @' not in status._json['full_text']:
        alltweet.append(status._json['full_text'])


#write tweets in csv file
with open("test.csv",'w') as f:
    writer = csv.writer(f, dialect='excel')
    for val in alltweet:
        lambda val: re.compile('\#').sub('', re.compile('RT @').sub('@', x).strip())
        writer.writerow([val])


# In[13]:





