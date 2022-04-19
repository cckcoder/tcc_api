from fastapi import FastAPI

from models.database import engine, Base
from models.inventory import inventory_model


from routers.inventory import inventory_router

app = FastAPI()
app.include_router(inventory_router.router)


@app.get("/")
def hello_word():
    return { "hello": "TCC" }

Base.metadata.create_all(engine)