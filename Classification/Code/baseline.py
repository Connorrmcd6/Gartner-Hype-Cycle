from functions import *


df = pd.read_csv('/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Classification/sentiment_test.csv')
df['subjectivity'] = df['text'].apply(base_subjectivity)
df['polarity'] = df['text'].apply(base_polarity)
df['sentiment'] = df['polarity'].apply(base_sentiment)

wordcloud(df)

sentibar(df)