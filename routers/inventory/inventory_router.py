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

@router.get("/{inventory_id}", response_model=InventoryDisplayBase)
def inventory_by_id(inventory_id: int, db: Session = Depends(get_db)):
    return inventory_controller.get_inventory_by_id(db, inventory_id)

@router.post("/")
def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.create_inventory(db, request)

@router.put("/{inventory_id}")
def update_name(inventory_id: int, request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.update_inventory(db, inventory_id, request)

@router.delete("/{inventory_id}")
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return inventory_controller.deleted_inventory(db, inventory_id)