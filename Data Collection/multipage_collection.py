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
keyword = "\"5g\" OR \"5G\" lang:en"

start_list =    ['2016-01-01T00:00:00.000Z',
                 '2016-02-01T00:00:00.000Z',
                 '2016-03-01T00:00:00.000Z',
                 '2016-04-01T00:00:00.000Z',
                 '2016-05-01T00:00:00.000Z',
                 '2016-06-01T00:00:00.000Z',
                 '2016-07-01T00:00:00.000Z',
                 '2016-08-01T00:00:00.000Z',
                 '2016-09-01T00:00:00.000Z',
                 '2016-10-01T00:00:00.000Z',
                 '2016-11-01T00:00:00.000Z',
                 '2016-12-01T00:00:00.000Z',
                 '2017-01-01T00:00:00.000Z',
                 '2017-02-01T00:00:00.000Z',
                 '2017-03-01T00:00:00.000Z',
                 '2017-04-01T00:00:00.000Z',
                 '2017-05-01T00:00:00.000Z',
                 '2017-06-01T00:00:00.000Z',
                 '2017-07-01T00:00:00.000Z',
                 '2017-08-01T00:00:00.000Z',
                 '2017-09-01T00:00:00.000Z',
                 '2017-10-01T00:00:00.000Z',
                 '2017-11-01T00:00:00.000Z',
                 '2017-12-01T00:00:00.000Z',
                 '2018-01-01T00:00:00.000Z',
                 '2018-02-01T00:00:00.000Z',
                 '2018-03-01T00:00:00.000Z',
                 '2018-04-01T00:00:00.000Z',
                 '2018-05-01T00:00:00.000Z',
                 '2018-06-01T00:00:00.000Z',
                 '2018-07-01T00:00:00.000Z',
                 '2018-08-01T00:00:00.000Z',
                 '2018-09-01T00:00:00.000Z',
                 '2018-10-01T00:00:00.000Z',
                 '2018-11-01T00:00:00.000Z',
                 '2018-12-01T00:00:00.000Z',
                 '2019-01-01T00:00:00.000Z',
                 '2019-02-01T00:00:00.000Z',
                 '2019-03-01T00:00:00.000Z',
                 '2019-04-01T00:00:00.000Z',
                 '2019-05-01T00:00:00.000Z',
                 '2019-06-01T00:00:00.000Z',
                 '2019-07-01T00:00:00.000Z',
                 '2019-08-01T00:00:00.000Z',
                 '2019-09-01T00:00:00.000Z',
                 '2019-10-01T00:00:00.000Z',
                 '2019-11-01T00:00:00.000Z',
                 '2019-12-01T00:00:00.000Z',
                 '2020-01-01T00:00:00.000Z',
                 '2020-02-01T00:00:00.000Z',
                 '2020-03-01T00:00:00.000Z',
                 '2020-04-01T00:00:00.000Z',
                 '2020-05-01T00:00:00.000Z',
                 '2020-06-01T00:00:00.000Z',
                 '2020-07-01T00:00:00.000Z',
                 '2020-08-01T00:00:00.000Z',
                 '2020-09-01T00:00:00.000Z',
                 '2020-10-01T00:00:00.000Z',
                 '2020-11-01T00:00:00.000Z',
                 '2020-12-01T00:00:00.000Z']

end_list =    ['2016-01-31T00:00:00.000Z',
                 '2016-02-28T00:00:00.000Z',
                 '2016-03-31T00:00:00.000Z',
                 '2016-04-30T00:00:00.000Z',
                 '2016-05-31T00:00:00.000Z',
                 '2016-06-30T00:00:00.000Z',
                 '2016-07-31T00:00:00.000Z',
                 '2016-08-31T00:00:00.000Z',
                 '2016-09-30T00:00:00.000Z',
                 '2016-10-31T00:00:00.000Z',
                 '2016-11-30T00:00:00.000Z',
                 '2016-12-31T00:00:00.000Z',
                 '2017-01-31T00:00:00.000Z',
                 '2017-02-28T00:00:00.000Z',
                 '2017-03-31T00:00:00.000Z',
                 '2017-04-30T00:00:00.000Z',
                 '2017-05-31T00:00:00.000Z',
                 '2017-06-30T00:00:00.000Z',
                 '2017-07-31T00:00:00.000Z',
                 '2017-08-31T00:00:00.000Z',
                 '2017-09-30T00:00:00.000Z',
                 '2017-10-31T00:00:00.000Z',
                 '2017-11-30T00:00:00.000Z',
                 '2017-12-31T00:00:00.000Z',
                 '2018-01-31T00:00:00.000Z',
                 '2018-02-28T00:00:00.000Z',
                 '2018-03-31T00:00:00.000Z',
                 '2018-04-30T00:00:00.000Z',
                 '2018-05-31T00:00:00.000Z',
                 '2018-06-30T00:00:00.000Z',
                 '2018-07-31T00:00:00.000Z',
                 '2018-08-31T00:00:00.000Z',
                 '2018-09-30T00:00:00.000Z',
                 '2018-10-31T00:00:00.000Z',
                 '2018-11-30T00:00:00.000Z',
                 '2018-12-31T00:00:00.000Z',
                 '2019-01-31T00:00:00.000Z',
                 '2019-02-28T00:00:00.000Z',
                 '2019-03-31T00:00:00.000Z',
                 '2019-04-30T00:00:00.000Z',
                 '2019-05-31T00:00:00.000Z',
                 '2019-06-30T00:00:00.000Z',
                 '2019-07-31T00:00:00.000Z',
                 '2019-08-31T00:00:00.000Z',
                 '2019-09-30T00:00:00.000Z',
                 '2019-10-31T00:00:00.000Z',
                 '2019-11-30T00:00:00.000Z',
                 '2019-12-31T00:00:00.000Z',
                 '2020-01-31T00:00:00.000Z',
                 '2020-02-28T00:00:00.000Z',
                 '2020-03-31T00:00:00.000Z',
                 '2020-04-30T00:00:00.000Z',
                 '2020-05-31T00:00:00.000Z',
                 '2020-06-30T00:00:00.000Z',
                 '2020-07-31T00:00:00.000Z',
                 '2020-08-31T00:00:00.000Z',
                 '2020-09-30T00:00:00.000Z',
                 '2020-10-31T00:00:00.000Z',
                 '2020-11-30T00:00:00.000Z',
                 '2020-12-31T00:00:00.000Z']

# start_list =    ['2020-05-01T00:00:00.000Z',
#                  '2020-06-01T00:00:00.000Z',
#                  '2020-07-01T00:00:00.000Z',
#                  '2020-08-01T00:00:00.000Z',
#                  '2020-09-01T00:00:00.000Z',
#                  '2020-10-01T00:00:00.000Z',
#                  '2020-11-01T00:00:00.000Z',
#                  '2020-12-01T00:00:00.000Z']

# end_list =    ['2020-05-31T00:00:00.000Z',
#                  '2020-06-30T00:00:00.000Z',
#                  '2020-07-31T00:00:00.000Z',
#                  '2020-08-31T00:00:00.000Z',
#                  '2020-09-30T00:00:00.000Z',
#                  '2020-10-31T00:00:00.000Z',
#                  '2020-11-30T00:00:00.000Z',
#                  '2020-12-31T00:00:00.000Z']

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

                df.to_sql('five_g', con=engine, if_exists='append', index=False, chunksize=1000)

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

                df.to_sql('five_g', con=engine, if_exists='append', index=False, chunksize=1000)
                
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

