import json
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import time
from functions import *

engine = create_engine('mysql+mysqlconnector://'+user+':'+passwd+'@'+ip+':3306/'+schema1)
cnxn = mysql.connector.connect(host = ip, user = user, password = passwd, database = schema1)

#Inputs for the request
bearer_token = bearer_token
headers = create_headers(bearer_token)
keyword = "machine learning lang:en"

start_list =    ['2021-01-01T00:00:00.000Z',
                 '2021-02-01T00:00:00.000Z',
                 '2021-03-01T00:00:00.000Z',
                 '2021-04-01T00:00:00.000Z',
                 '2021-05-01T00:00:00.000Z',
                 '2021-06-01T00:00:00.000Z',
                 '2021-07-01T00:00:00.000Z',
                 '2021-08-01T00:00:00.000Z',
                 '2021-09-01T00:00:00.000Z',
                 '2021-10-01T00:00:00.000Z',
                 '2021-11-01T00:00:00.000Z',
                 '2021-12-01T00:00:00.000Z']

end_list =    ['2021-01-31T00:00:00.000Z',
                 '2021-02-28T00:00:00.000Z',
                 '2021-03-31T00:00:00.000Z',
                 '2021-04-30T00:00:00.000Z',
                 '2021-05-31T00:00:00.000Z',
                 '2021-06-30T00:00:00.000Z',
                 '2021-07-31T00:00:00.000Z',
                 '2021-08-31T00:00:00.000Z',
                 '2021-09-30T00:00:00.000Z',
                 '2021-10-31T00:00:00.000Z',
                 '2021-11-30T00:00:00.000Z',
                 '2021-12-31T00:00:00.000Z']
max_results = 500


#Total number of tweets we collected from the loop
total_tweets = 0

for i in range(0, len(start_list)):

    st = start_list[i]
    ed = end_list[i]

    # Inputs
    count = 0 # Counting tweets per time period
    max_count = 200000 # Max tweets per time period
    flag = True
    next_token = None

    # Check if flag is true
    while flag:
        # Check if max_count reached
        if count >= max_count:
            break
        print("-------------------")
        print("Token: ", next_token)
        url = create_url(keyword, st, ed, max_results)
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                print("Start Date: ", st)
                ids = []
                date = []
                like_count = []
                quote_count = []
                reply_count = []
                retweet_count = []
                text = []

                for i in json_response['data']:
                    ids.append(i['id'])
                    date.append(i['created_at'].split('T')[0])
                    like_count.append(i['public_metrics']['like_count'])
                    quote_count.append(i['public_metrics']['quote_count'])
                    reply_count.append(i['public_metrics']['reply_count'])
                    retweet_count.append(i['public_metrics']['retweet_count'])
                    text.append(deEmojify(cleanTxt(i['text'])))

                db_insert = {}

                db_insert["id"] = ids
                db_insert["date"] = date
                db_insert["like_count"] = like_count
                db_insert["quote_count"] = quote_count
                db_insert["reply_count"] = reply_count
                db_insert["retweet_count"] = retweet_count
                db_insert["text"] = text

                df = pd.DataFrame.from_dict(db_insert)

                df.to_sql('machine_learning', con=engine, if_exists='append', index=False, chunksize=1000)

                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(20)                
        # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------")
                print("Start Date: ", st)
                ids = []
                date = []
                like_count = []
                quote_count = []
                reply_count = []
                retweet_count = []
                text = []

                for i in json_response['data']:
                    ids.append(i['id'])
                    date.append(i['created_at'].split('T')[0])
                    like_count.append(i['public_metrics']['like_count'])
                    quote_count.append(i['public_metrics']['quote_count'])
                    reply_count.append(i['public_metrics']['reply_count'])
                    retweet_count.append(i['public_metrics']['retweet_count'])
                    text.append(deEmojify(cleanTxt(i['text'])))

                db_insert = {}

                db_insert["id"] = ids
                db_insert["date"] = date
                db_insert["like_count"] = like_count
                db_insert["quote_count"] = quote_count
                db_insert["reply_count"] = reply_count
                db_insert["retweet_count"] = retweet_count
                db_insert["text"] = text

                df = pd.DataFrame.from_dict(db_insert)

                df.to_sql('machine_learning', con=engine, if_exists='append', index=False, chunksize=1000)
                
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(20)
            
            #Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        time.sleep(20)
print("Total number of results: ", total_tweets)

