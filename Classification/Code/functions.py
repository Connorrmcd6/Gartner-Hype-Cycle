import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from sklearn.utils import shuffle
import re
import nltk
import time
import warnings
warnings.filterwarnings("ignore")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import LancasterStemmer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import xgboost as xgb
from sklearn.svm import LinearSVC
from lightgbm import LGBMClassifier
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split



def base_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def base_polarity(text):
    return TextBlob(text).sentiment.polarity

def base_sentiment(score):
    if score < 0:
        return 0
    if score == 0:
        return 1
    if score > 0:
        return 2

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


# Global Parameters
stop_words = set(stopwords.words('english'))

def load_dataset(filename, cols):
    dataset = pd.read_csv(filename, encoding='latin-1')
    dataset.columns = cols
    return dataset

def remove_unwanted_cols(dataset, cols):
    for col in cols:
        del dataset[col]
    return dataset

def preprocess_tweet_text(tweet):
    tweet = tweet.lower()
    # Remove urls
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    # Remove user @ references and '#' from tweet
    tweet = re.sub(r'\@\w+|\#','', tweet)
    # Remove punctuations
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    tweet_tokens = word_tokenize(tweet)
    filtered_words = [w for w in tweet_tokens if not w in stop_words]
    
    ps = PorterStemmer()
    filtered_words2 = [ps.stem(w) for w in filtered_words]
    # lemmatizer = WordNetLemmatizer()
    # filtered_words = [lemmatizer.lemmatize(w, pos='a') for w in filtered_words]
    
    return " ".join(filtered_words2)

def get_feature_vector(train_fit):
    vector = TfidfVectorizer(sublinear_tf=True)
    vector.fit(train_fit)
    return vector

def convert_sent(sentiment):
    if sentiment == 2:
        return 1
    elif sentiment == 4:
        return 2

def preprocess(text):
    review = re.sub('[^a-zA-Z]',' ',text) 
    review = review.lower()
    review = review.split()
    ps = LancasterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    return ' '.join(review)