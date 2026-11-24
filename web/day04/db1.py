import sqlite3

conn = sqlite3.connect("todos.db")

conn.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, text TEXT, done INTEGER DEFAULT 0)")
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("学SQlite第一天", 0))
conn.commit()

conn.close()
print("脚本跑完了") 