from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello():
    return { "Hello": "World" }


@app.get("/{name}")
def hello_name(name: str):
    return { "hello": name}

@app.post("/")
def create_name():
    return { "hello": "post" }

@app.put("/")
def update_name():
    return { "hello": "put"}

@app.delete("/")
def delete_name():
    return { "hello": "delete"}