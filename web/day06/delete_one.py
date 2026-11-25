import sqlite3

conn = sqlite3.connect("../day04/todos.db")
cur = conn.cursor()

conn.execute("DELETE FROM todos WHERE id = ?", (2,))
conn.commit()

conn.close()
print("id = 2 已删除")