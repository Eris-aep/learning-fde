import sqlite3

conn = sqlite3.connect("todos.db")
cur = conn.cursor()

cur.execute("SELECT * FROM todos")
rows = cur.fetchall()

print("共", len(rows), "条")
for row in rows:
    print(row)

conn.close()