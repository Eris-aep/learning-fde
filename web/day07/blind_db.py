import sqlite3

conn = sqlite3.connect("day07.db")

conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, text TEXT, done INTEGER DEFAULT 0)")
conn.execute("INSERT INTO todos(text, done) VALUES(?, ?)", ("复习接口",0))
conn.execute("INSERT INTO todos(text, done) VALUES(?, ?)", ("复习数据库", 1))
conn.commit()

rows = conn.execute("SELECT * FROM todos WHERE done = 0").fetchall()
print("未完成的有", len(rows), "条：")
for row in rows:
    print(row)

conn.close()