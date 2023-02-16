import sqlite3

# Assume the 'name' variable is received from user input
name = "John"

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# This query is vulnerable to SQL injection attacks
cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
