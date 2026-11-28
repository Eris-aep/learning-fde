# ============================================
# day11 读代码素材（第 1 级：约 45 行，带注释）
# 内容：一个带 4 个接口的待办小应用（接口 + 数据库）
# 里面埋了 1 个 bug：能跑通、不报错，但有一个功能"点了没反应"
# ============================================

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
conn = sqlite3.connect("demo11.db", check_same_thread=False)

conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, text TEXT, done INTEGER DEFAULT 0)")
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("买菜", 0))
conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", ("写作业", 1))
conn.commit()

class NewTodo(BaseModel):
    text: str

# 接口1：查全部
@app.get("/todos")
def list_todos():
    rows = conn.execute("SELECT * FROM todos").fetchall()
    result = []
    for row in rows:
        result.append({"id": row[0], "text": row[1], "done": row[2]})
    return result

# 接口2：新增一条
@app.post("/todos")
def add_todo(item: NewTodo):
    conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", (item.text, 0))
    conn.commit()
    return {"ok": True}

# 接口3：把某条标记为完成
@app.post("/todos/{todo_id}/done")
def mark_done(todo_id: int):
    conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    return {"ok": True} 

# 接口4：删除一条
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    return {"ok": True}


@app.get("/todos/undone")
def list_todos():
    rows = conn.execute("SELECT * FROM todos WHERE done = 0").fetchall()
    result = []
    for row in rows:
        result.append({"id": row[0], "text": row[1], "done": row[2]})
    return result
