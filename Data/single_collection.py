import json
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from functions import *

engine = create_engine('mysql+mysqlconnector://'+user+':'+passwd+'@'+ip+':3306/'+schema1)
cnxn = mysql.connector.connect(host = ip, user = user, password = passwd, database = schema1)

#Inputs for the request
bearer_token = bearer_token
headers = create_headers(bearer_token)
# keyword = "machine learning lang:en"
keyword = "machine learning lang:en"
start_time = time_convert('2022-02-02 00:00:00') #(ISO 8601/RFC 3339)
end_time =  time_convert('2022-02-07 00:00:00')
max_results = 10

url = create_url(keyword, start_time,end_time, max_results)

json_response = connect_to_endpoint(url[0], headers, url[1])


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

