import sqlite3

conn = sqlite3.connect("../day04/todos.db")

conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (3,))
conn.commit()

conn.close()
print("id = 3 已更成完成")