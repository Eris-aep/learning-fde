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