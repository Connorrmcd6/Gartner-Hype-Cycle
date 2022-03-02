from functions import *
from sqlalchemy import create_engine, false
from db_config import *

engine = create_engine('mysql+mysqlconnector://'+ user + ':' + passwd + '@' + ip + ':3306/' + schema1)
df = pd.read_sql('SELECT * FROM short_ml', engine)

df['polarity'] = df['text'].apply(base_polarity)
df['sentiment'] = df['polarity'].apply(base_sentiment)

wordcloud(df)

sentibar(df)

# short_sentiment = df.iloc[:, [0,8]]

# short_sentiment.to_sql('base_sentiment' , con=engine, if_exists='append', index=false, chunksize=20000)

print('done')