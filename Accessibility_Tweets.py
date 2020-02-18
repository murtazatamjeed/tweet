# Author: Murtaza Tamjeed
# Retrieving Accessibility Tweets

import os
import pandas as pd
import tweepy


# Twitter credentials
consumer_key = "WbNc21cbX0WXAafRuVxv6u9Hw" #twitter app’s API Key
consumer_secret = "ZIK1R2tPXOMzYgx0TiWDrTDNjwzIZNafQqtUrND0loKMHHdJR9" #twitter app’s API secret Key
access_token = "1036298258782597121-na3oGLHa7wdqdpB3Eyd1GuzgFbgvZp" #twitter app’s Access token
access_token_secret = "TGl6UQ2e5uUUhGtJXWFs0GUMOwh0UWohkg1Fj8Ri8wBpV" #twitter app’s access token secret

# Pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# CSV file to export tweets to
accessibility_tweets = "accessibility_tweets.csv"
# Columns in CSV file
COLS = ['created_at', 'tweet_text', 'retweet_count', 'author', 'hashtags']
# Date for tweets
start_date = '2020-01-01'


# Method to write tweets
def write_tweets(keyword, file):
    # If the file exists, then read the existing data from the CSV file.
    if os.path.exists(file):
        df = pd.read_csv(file, header=0)
    else:
        df = pd.DataFrame(columns=COLS)
    # page attribute in tweepy.cursor and iteration
    for tweets in tweepy.Cursor(api.search, q=keyword,
                                            count=100,
                                            include_rts=False,
                                            since=start_date).pages(10):
        for status in tweets:
            new_entry = []
            status = status._json

            # check whether the tweet is in english or skip to the next tweet
            if status['lang'] != 'en':
                continue

            # new entry append
            new_entry += [status['created_at'],
                          status['text'],
                          status['retweet_count']]

            # to append original author of the tweet
            new_entry.append(status['user']['screen_name'])

            # hashtagas are saved using space separated
            hashtags = " ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])
            new_entry.append(hashtags)

            single_tweet_df = pd.DataFrame([new_entry], columns=COLS)
            df = df.append(single_tweet_df, ignore_index=True)
            csvFile = open(file, 'a', encoding='utf-8')
    df.to_csv(csvFile, mode='a', columns=COLS, index=False, encoding="utf-8")


# declare keywords for search
accessibility_keywords = "Accessibility"

# call main method passing keywords and file name
write_tweets(accessibility_keywords, accessibility_tweets)

