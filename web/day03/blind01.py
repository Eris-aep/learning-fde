from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "你好，Eris"

me = {"名字":"Eris", "性别":"男"}
@app.get("/me")
def dicts():
    return me

@app.get("/add")
def add(a:int, b:int):
    return a + b