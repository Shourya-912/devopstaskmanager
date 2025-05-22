import mysql.connector
import time
from config import DB_CONFIG

def get_connection():
    retries = 10
    for i in range(retries):
        try:
            return mysql.connector.connect(
                host = DB_CONFIG['host'],
                user = DB_CONFIG['user'],
                password = DB_CONFIG['password'],
                database = DB_CONFIG['database']
            ) 
        except mysql.connector.Error as err:
            print("MySQL is not ready (attempt {i+1}/{retries}) -retrying in 5 seconds")
            time.sleep(5)
            retries-=1
    raise Exception("Failed to connect to MySQL after several retries")
