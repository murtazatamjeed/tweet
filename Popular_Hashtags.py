# Author: Murtaza Tamjeed
# Trending Hashtags Related to Accessibility

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Reading CSV file (containing tweets) into a Data Frame
df = pd.read_csv("accessibility_tweets.csv")
df = df.dropna()
all_hashtags = df['hashtags']
# print(all_hashtags)

# Lowercase hashtags
words = df['lower_hashtags'] = df['hashtags'].str.lower().apply(lambda x:''.join([word for word in str(x)]))

# Count_of_hashtags
count_of_hashtags = df['lower_hashtags'].str.split(expand=True).stack().value_counts()


def top_hashtags():
    top_ten = count_of_hashtags.nlargest(22)
    print(top_ten)
    fig, ax = plt.subplots(figsize=(12, 8))
    # Plot horizontal bar graph
    top_ten.sort_values().plot.barh()
    ax.set_title("Top Accessibility Hashtags")
    plt.show()


def trending_hashtags():
    # Reading the CSV/JSON files into DataFrames
    df = pd.read_csv("top10_chart.csv", index_col=0)
    labels = df.index
    values = df['count']
    # Use hole to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text="Trending Accessibility Hashtags")
    fig.show()


top_hashtags()
trending_hashtags()


