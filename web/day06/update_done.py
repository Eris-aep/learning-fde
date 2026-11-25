import sqlite3

conn = sqlite3.connect("../day04/todos.db")
cur = conn.cursor()

conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (1,))
conn.commit()

conn.close()
print("id = 1 已标记完成")