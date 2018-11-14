
# coding: utf-8

# In[24]:



from TwitterSearch import *
import csv
import json
import tweepy


#This code search twitter for keywords to identify users who have shared their mental health diagnosis

m = [] #list of match tweet's text
l = [] #list of match tweet's Username
label = []  #list of disease
try:
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
    
      # create a TwitterSearch object with our secret tokens ()
    ts = TwitterSearch(
        consumer_key = 'jxpGx90bgjqZDiRcdiT2uLUO9',
        consumer_secret = 'DPI1QRcRE5CP37IaLDxJpRT0s3k0Dv1H2alhHWlPwCnt5PW81n',
        access_token = '1396904694-SHm12SMxHJwhKT7fB5ivv0P9IHvZIC753wDMWT5',
        access_token_secret = 'ejVaIC7oMmfyUiT6gYwlOUp6VpoFeMjkB3f5MviT0z0Sx'
     )
    
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with Anxiety' ]) # let's define words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

   

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(0)#anxiety
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(0)#anxiety
  

    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with depression']) # let's define words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(1)#depression
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(1)#depression
    
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with dep']) # let's define words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(1)#depression
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(1)#depression

   
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with Bipolar' ])
    tso.set_language('en')
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(2)#bipolar
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(2)#bipolar

  
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with post-traumatic stress disorder' ])
    tso.set_language('en')
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(3)#ptsd
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(3)#ptsd


    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with PTSD' ])
    tso.set_language('en')
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(3)#ptsd
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(3)#ptsd

  
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with ADHD' ])
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(4)#adhd
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(4)#adhd

    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I have been diagnosed with Attention Deficit Hyperactivity Disorder'])
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False)

    for tweet in ts.search_tweets_iterable(tso):
        if not tweet['retweeted'] and 'RT @' not in tweet['text']:
            l.append(tweet['user']['screen_name'])
            m.append(tweet['text'])
            label.append(4)#adhd
            for status in tweepy.Cursor(api.user_timeline, screen_name=tweet['user']['screen_name'], tweet_mode='extended').items(200):
                if not status.retweeted and 'RT @' not in status._json['full_text']:
                    l.append(tweet['user']['screen_name'])
                    m.append(status._json['full_text'])
                    label.append(4)#adhd


except TwitterSearchException as e: # take care of all those ugly errors if there are some
   print(e)


with open('Data.csv', 'w', newline='') as csvfile:
    fieldnames = ['disease','username', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i, j, k in zip(l, m,label):
        writer.writerow({'disease': k,'username': i, 'text': j})
    print("done writing")

