from pydantic import BaseModel
from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("../day04/todos.db", check_same_thread = False)

@app.get("/todos")
def list_todos():
    rows = conn.execute("SELECT * FROM todos").fetchall()
    result = []
    for row in rows:
        result.append({"id": row[0], "text": row[1], "done": row[2]})
    return result

class NewTodo(BaseModel):
    text: str

@app.post("/todos")
def add_todo(item: NewTodo):
    conn.execute("INSERT INTO todos (text, done) VALUES (?, ?)", (item.text, 0))
    conn.commit()
    return {"ok", True}
