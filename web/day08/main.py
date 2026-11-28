from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import sqlite3, logging

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s, %(levelname)s, %(message)s",
    encoding = "utf-8"
)

app = FastAPI()

conn = sqlite3.connect("../day04/todos.db", check_same_thread = False)

@app.get("/todos")
def list_todos():
    rows = conn.execute("SELECT * FROM todos").fetchall()
    result = []
    for row in rows:
        result.append({"id": row[0], "text": row[1], "done": row[2]})
    logging.info("GET /todos 返回 %d 条", len(result))
    return result

class NewTodo(BaseModel):
    text: str

@app.post("/todos")
def add_todo(item: NewTodo):
    if item.text.strip() == "":
        raise HTTPException(status_code = 400, detail="标题不能为空")
    conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", (item.text, 0))
    conn.commit()
    return {"ok": True}


@app.post("/todos/{todo_id}/done")
def mark_done(todo_id: int):
    cur = conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code = 404, detail = f"id = {todo_id}的待办不存在")
    return {"ok": True}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    cur = conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code = 404, detail=f"id = {todo_id}的待办不存在")
    return {"ok": True}

