import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        page INTEGER,
        current_page INTEGER
    )
    """)

cursor.execute ("""
    INSERT INTO books VALUES(
        0 

    )
    """)