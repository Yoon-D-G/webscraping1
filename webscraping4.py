import mysql.connector as mysql
from webscraping3 import complete_dictionary as complete_dict


db = mysql.connect(
    host = 'localhost',
    user = 'EDG',
    passwd = 'ABCeasyas123!',
    database = 'all_books'
)


cursor = db.cursor()


cursor.execute('CREATE DATABASE all_books')

