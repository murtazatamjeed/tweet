# TRENDING ACCESSIBILITY HASHTAGS

This is a machine learning project that aims to extract the trending accessibility related hashtags from tweets.
# Dataset
The dataset used for this project is a collection of around 1000 recent tweets retrieved from twitter using twitter developer credentials.
While collecting the tweets we considered to only search for the tweets that contained the word "accessibility".

## Credentials
To follow with this project you will need to have following twitter developer app's credentials in order to retrieve tweets.
* consumer key
* consumer secret
* access token
* access token secret

In addition, you will need to create a Microsoft Azure account and have the following credentials to be able to use Azure machine learning services.
* subscription key
* service URL

## Libraries
This project uses Python 3.7 with following libraries:
* Tweepy
* Pandas
* OS
* Matplotlib
* Plotly
* Requests
* wordCloud
* Numpy
* PIL

## Running the source code
This project contains four essential python files that can be run independent of each other. 
* Run the "Accessibility_Tweets.py" python file available under main directory to search, retrieve and export tweets into a csv file.
* For performing sentiment analysis on the retrieved tweets, run the file "Sentiment_Analysis.py" available under the main directory.
* For extracting popular hashtags from the tweets that we just retrieved, run the file called "Popular_Hashtags.py". This file consists of two methods; 1) top_hashtags() which extracts top 20 popular hashtags and plots a horizontal bar graph form the data; 2) trending_hashtags() extracts top 10 (trending) hashtags and plots them a pie chart. 
* By running the "word_cloud.py" file, you can generate a word cloud of all the hashtags extracted from the tweets.
