from fastapi import FastAPI

app = FastAPI()

lists = {"姓名": "Eris", "城市": "魔大陆", "目标": "最强剑圣"}

@app.get("/hello")
def hello():
    return "接口已接通"

@app.get("/me")
def me():
    return lists

@app.get("/add")
def add(a:int, b:int):
    return a + b
