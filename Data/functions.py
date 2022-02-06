import requests
import re
from datetime import datetime
from configs import *


def time_convert(time):
    time = time.replace(" ", "T")
    time += 'Z'
    return time

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    # search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from
    search_url = "https://api.twitter.com/2/tweets/search/recent" #Change to the endpoint you want to collect data from

    keyword += ' -is:retweet -is:reply'

    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'tweet.fields': 'id,text,created_at,public_metrics',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #removes mentions
    text = re.sub(r'#', '', text) #removes hashtags
    text = re.sub(r'RT[\s]+', '', text) #removes retweet symbol from start
    text = re.sub(r'https?:\/\/\S+', '', text) #removes links
    text = re.sub(r'[^\w\s]', '', text) #removes all punctuation
    text = text.lower() #converts all to lower
    return text

def deEmojify(text):
    return text.encode('ascii', 'ignore').decode('ascii')