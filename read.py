import sqlite3
import sys

conn = sqlite3.connect('music.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM songs")

    while True:
        row = cur.fetchone()

        if row == None:
            break
        print row[0], row[1], row[2]
