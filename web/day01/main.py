from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"msg": "你好"}


@app.get("/me")
def me():
    return {"姓名": "Eris", "城市": "魔大陆" , "目标": "FDE"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
