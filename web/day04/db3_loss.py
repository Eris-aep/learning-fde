import sqlite3

conn = sqlite3.connect("todos.db")

# conn.execute("CREATE TABLE IF NOT INEGER todos (id INTEGER PRIMARY KEY, text TEXT, done INTEGER DEFAULT 0)")
conn.execute("INSERT INTO todos (text, done) VALUES(?, ?)", ("这条会丢", 0))

conn.close()
print("跑完了（但是我没 commit）")