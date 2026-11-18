from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"status": "OK"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/message")
def message(data: dict):
    print(data)
    return {"received": data}
