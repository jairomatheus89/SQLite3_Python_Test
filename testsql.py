import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

result = cursor.execute('INSERT INTO users (name) SELECT "jairote" WHERE NOT EXISTS (SELECT 1 FROM users WHERE name = "jairo"')
                        

conn.close()