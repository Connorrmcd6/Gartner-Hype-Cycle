from functions import *
from sqlalchemy import create_engine
from db_config import *


table = 'machine_learning'
classifier_name = 'base'
start_date = '2021-01-01'
end_date = '2021-12-31'

engine = create_engine('mysql+mysqlconnector://'+ user + ':' + passwd + '@' + ip + ':3306/' + schema1)
df = pd.read_sql(f'SELECT * FROM {table} WHERE date >= \'{start_date}\' AND date <= \'{end_date}\'', engine)

df['polarity'] = df['text'].apply(base_polarity)
df['sentiment'] = df['polarity'].apply(base_sentiment)


sentiment = df.iloc[:, [0,-1]]

sentiment.to_sql(f'{classifier_name}_sentiment' , con=engine, if_exists='append', index=False, chunksize=20000)

print('done')