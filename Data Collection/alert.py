import mysql.connector
from functions import *

cnxn = mysql.connector.connect(host = ip, user = user, password = passwd, database = schema1)

cursor = cnxn.cursor()
statement1 = 'SELECT COUNT(1) FROM social.five_g;'
statement1b = 'SELECT MAX(date) FROM social.five_g;'
cursor.execute(statement1)
new_count = cursor.fetchone()[0]

cursor.execute(statement1b)
max_date = cursor.fetchone()[0]

statement2 = 'SELECT MAX(tweet_count) FROM social.logs;'
cursor.execute(statement2)
old_count = cursor.fetchone()[0]

if new_count <= old_count:
    max_date = str(max_date)
    max_date = max_date.replace('-', '\\-')
    message = f'🚨 *TWITTER DATA COLLECTION HAS STOPPED\\!*\nStopped at: {max_date}'
    telegram_bot_sendtext(message, chat_id)
    statement3 = 'INSERT INTO social.logs (tweet_count) VALUES (' + str(new_count) + ')'
    cursor.execute(statement3)
    cnxn.commit()
    print('stopped')

else:
    x = ''
    statement3 = 'INSERT INTO social.logs (tweet_count) VALUES (' + str(new_count) + ')'
    cursor.execute(statement3)
    cnxn.commit()
    print('run successfully')


cnxn.close()