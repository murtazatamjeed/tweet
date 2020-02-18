# Author: Murtaza Tamjeed
# Sentiment Analysis of Accessibility Tweets

import pandas as pd
import requests

subscription_key = "Your subscription key"
sentiment_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment"

# Reading CSV file (containing tweets) into a Data Frame
df = pd.read_csv("accessibility_tweets.csv")
# print(df)

documents = {"documents": []}

for idx, row in df.iterrows():
    documents["documents"].append({
        "id": str(idx + 1),
        "text": row["tweet_text"]
    })

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
# pprint(sentiments)

sentiment_df = pd.DataFrame([d["score"] for d in sentiments["documents"]], index=[d["id"] for d in sentiments["documents"]],
             columns=["sentiment_score"])
print(sentiment_df)
sentiment_df["sentiment_percentage"] = round(sentiment_df.sentiment_score * 100, 2)
print(sentiment_df)
print(sentiment_df.sentiment_percentage.describe())
