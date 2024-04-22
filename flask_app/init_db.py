import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO requests (title, content) VALUES (?, ?)",
            ('First Request', 'Content for the first request')
            )

cur.execute("INSERT INTO requests (title, content) VALUES (?, ?)",
            ('Second Request', 'Content for the second request')
            )

connection.commit()
connection.close()