import mysql.connector
import time
from config import DB_CONFIG

def get_connection():
    retries = 5
    while retries>0:
        try:
            return mysql.connector.connect(
                host = DB_CONFIG['host'],
                user = DB_CONFIG['user'],
                password = DB_CONFIG['password'],
                database = DB_CONFIG['database']
            ) 
        except mysql.connector.Error as err:
            print("MySQL is not ready retrying in 5 seconds")
            time.sleep(5)
            retries-=1
    raise Exception("Failed to connect to MySQL after several retries")
