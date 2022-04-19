from fastapi import APIRouter
from pydantic import BaseModel

from models.inventory.inventory_model import InventoryBase, InventoryDisplayBase

router = APIRouter(
    prefix="/inventory", tags=["inventory"]
)



@router.get("/")
def all_inventory():
    pass

@router.get("/{id}")
def inventory_by_id(id: int):
    pass

@router.post("/")
def create_inventory(request: InventoryBase):
    return request

@router.put("/{id}")
def update_name(id: int):
    pass

@router.delete("/{id}")
def delete_inventory(id: int):
    pass