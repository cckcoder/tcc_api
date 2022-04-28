from fastapi import FastAPI

from models.database import engine, Base
from models.users import users_model

from routers.inventory import inventory_router
from routers.users import users_router

app = FastAPI()
app.include_router(inventory_router.router)
app.include_router(users_router.router)


@app.get("/")
def hello_word():
    return {"hello": "TCC"}


# Base.metadata.create_all(engine)
users_model.Base.metadata.create_all(engine)
