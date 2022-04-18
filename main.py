from fastapi import FastAPI

from routers import inventory_router

app = FastAPI()
app.include_router(inventory_router.router)


@app.get("/")
def hello_word():
    return { "hello": "TCC" }