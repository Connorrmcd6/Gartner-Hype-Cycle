import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from functions import *

engine = create_engine('mysql+mysqlconnector://'+user+':'+passwd+'@'+ip+':3306/'+schema2)
cnxn = mysql.connector.connect(host = ip, user = user, password = passwd, database = schema2)

df = pd.read_csv('/Users/connormcdonald/Desktop/Masters/MIT807/Gartner Repository/Data/academic_data.csv')


df['Abstract'] = df['Abstract'].apply(cleanTxt).apply(deEmojify)

df.to_sql('machine_learning', con=engine, if_exists='append', index=True, chunksize=1000)
print('done')

