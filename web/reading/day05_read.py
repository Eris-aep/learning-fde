# ============================================
# day05 读代码素材（第 1 级：约 30 行，带注释）
# 内容：用 SQLite 存待办的小脚本
# 里面埋了 1 个 bug：能跑通、不报错，但打印结果不对劲
# ============================================

import sqlite3

conn = sqlite3.connect("reading_demo.db")

# 1. 建表：id 自动编号，text 存内容，done 记完成状态（0=没做完，1=做完了）
conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, text TEXT, done INTEGER DEFAULT 0)")

# 2. 插入三条测试数据
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("买菜", 0))
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("写作业", 1))
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("早睡", 0))
conn.commit()

# 3. 只查「没做完」的待办（done = 0 就是没做完）
cur = conn.cursor()
cur.execute("SELECT * FROM todos WHERE done = 1")
rows = cur.fetchall()

# 4. 一条一条打印出来
print("已完成的有", len(rows), "条：")
for row in rows:
    print(row)

conn.close()