import mysql.connector
from functions import *

cnxn = mysql.connector.connect(host = ip, user = user, password = passwd, database = schema1)

cursor = cnxn.cursor()
statement1 = 'SELECT COUNT(1) FROM social.machine_learning;'
cursor.execute(statement1)
new_count = cursor.fetchone()[0]

statement2 = 'SELECT MAX(tweet_count) FROM social.logs;'
cursor.execute(statement2)
old_count = cursor.fetchone()[0]

if new_count == old_count:
    message = '🚨 *TWITTER DATA COLLECTION HAS STOPPED!*'
    telegram_bot_sendtext(message, chat_id)
    print('stopped')

else:
    statement3 = 'INSERT INTO social.logs (tweet_count) VALUES (' + str(new_count) + ')'
    cursor.execute(statement3)
    cnxn.commit()
    print('run successfully')


cnxn.close()