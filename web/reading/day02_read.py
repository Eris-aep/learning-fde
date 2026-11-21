# ============================================
# day02 读代码素材：内存版「待办清单」
# 数据不进数据库，全存在一个列表里（列表套字典，Day 21 的旧知识）
# 里面 4 个接口，有 1 个是坏的：能启动、不报错、但功能永远不生效
# ============================================

from fastapi import FastAPI

app = FastAPI()

# ---------- 数据区：所有待办都在这个列表里 ----------
todos = [
    {"id": 1, "text": "跑通第一个接口", "done": True},
    {"id": 2, "text": "提交day01", "done": True},
    {"id": 3, "text": "读完这段代码", "done": False},
]

# ---------- 工具函数：按编号找待办 ----------
# 找到：返回那个字典；找不到：返回 None（表示"没有这条"）
def find_todo(tid):
    for t in todos:
        if t["id"] == tid:
            return t
    return None

# ---------- 接口 1：列出所有没完成的 ----------
@app.get("/list")
def list_todos():
    result = []
    for t in todos:
        if not t["done"]:
            result.append(t)
    return {"count": len(result), "items": result}

# ---------- 接口 2：新增一条，编号自动算 ----------
@app.get("/add_todo")
def add_todo(text):
    todo = {"id": len(todos) + 1, "text": text, "done": False}
    todos.append(todo)
    return {"ok": True, "new_id": todo["id"]}

# ---------- 接口 3：把某一条标记为完成 ----------
@app.get("/done")
def done(id:int): 
    t = find_todo(id)
    if t is None:
        return {"ok": False, "msg": "找不到这条待办"}
    t["done"] = True
    return {"ok": True}

# ---------- 接口 4：统计 ----------
@app.get("/stats")
def stats(): 
    done_count = 0
    for t in todos:
        if t["done"]:
            done_count = done_count + 1
    return {"total": len(todos), "done": done_count, "undone": len(todos) - done_count}
