import sqlite3

conn = sqlite3.connect('music.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE songs(SONG_NO INT, SONG_NAME TEXT, SONG_ARTIST TEXT, SONG_GENRE TEXT, SONG_YEAR YEAR)")

def tableCreateUser():
    c.execute("CREATE TABLE usersongs(SONG_NO INT, SONG_NAME TEXT, SONG_ARTIST TEXT, SONG_GENRE TEXT, SONG_YEAR YEAR)")

def dataEntry():
    c.execute("INSERT INTO songs VALUES(1, 'Hello', 'Adele', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(2, 'Sorry', 'Justin Bieber', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(3, 'Love Yourself', 'Justin Bieber', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(4, 'Hotline Bling', 'Drake', 'Rap', 2015)")
    c.execute("INSERT INTO songs VALUES(5, 'What Do You Mean?', 'Justin Bieber', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(6, 'Same Old Love', 'Selena Gomez', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(7, 'Here', 'Alessia Cara', 'Pop', 2015)")
    c.execute("INSERT INTO songs VALUES(8, 'Stitches', 'Shawn Mendes', 'Country', 2015)")
    c.execute("INSERT INTO songs VALUES(9, 'The Hills', 'The Weeknd', 'Pop', 2015)")
    conn.commit()

def dataEntryUser():
    c.execute("INSERT INTO usersongs VALUES(1, 'Kate (2015 Remix)', 'Arty', 'Trance', 2015)")
    c.execute("INSERT INTO usersongs VALUES(2, 'Mezzo Forte', 'Nick Sember', 'Trance', 2015)")
    conn.commit()

def run():
    tableCreate()
    tableCreateUser()
    dataEntry()
    dataEntryUser()
