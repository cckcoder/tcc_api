from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

from sqlalchemy.orm import Session
from models.database import get_db

from models.inventory.inventory_model import InventoryBase, InventoryDisplayBase

from routers.inventory import inventory_controller

router = APIRouter(
    prefix="/inventory", tags=["inventory"]
)


@router.get("/", response_model=List[InventoryDisplayBase])
def all_inventory(db: Session = Depends(get_db)):
    return inventory_controller.get_all_inventory(db)

@router.get("/{id}")
def inventory_by_id(id: int):
    pass

@router.post("/")
def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.create_inventory(db, request)

@router.put("/{id}")
def update_name(id: int):
    pass

@router.delete("/{id}")
def delete_inventory(id: int):
    pass