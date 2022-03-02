import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob


def base_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def base_polarity(text):
    return TextBlob(text).sentiment.polarity


def base_sentiment(score):
    if score < 0:
        return 'negative'
    if score == 0:
        return 'neutral'
    if score > 0:
        return 'positive'

def wordcloud(df):
    allwords = ' '.join([tweets for tweets in df['text']]) 
    wordCloud = WordCloud(width =500, height = 300, random_state = 21, max_font_size = 119).generate(allwords)
    plt.imshow(wordCloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.show()

def sentibar(df):
    df['sentiment'].value_counts()
    plt.title('sentiment analysis')
    plt.xlabel('sentiment')
    plt.ylabel('counts')
    df['sentiment'].value_counts().plot(kind='bar')
    plt.show()

