import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            ('Amal', 'amal@gmail.com', 'password123')
            )

cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            ('Kamal', 'kamal@gmail.com', 'password456')
            )

connection.commit()
connection.close()