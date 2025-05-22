# config.py
 
import os
from dotenv import load_dotenv
 
load_dotenv()  # Load .env variables
 
DB_CONFIG = {
    "host": "mysql",
    "database": os.getenv("MYSQL_NAME"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD")
}
