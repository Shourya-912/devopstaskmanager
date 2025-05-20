from db import get_connection

def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("create table if not exists users(id int auto_increment primary key, name varchar(100), email varchar (100) unique);")

    conn.commit()
    conn.close() 