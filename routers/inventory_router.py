from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/inventory", tags=["inventory"]
)

class Inventory(BaseModel):
    description: str
    price: float

inventory = [
    { "description": "pencil", "price": 14 },
    { "description": "ruler", "price": 21 },
    { "description": "pen", "price": 34 },
]

@router.get("/")
def all_inventory():
    return inventory

@router.get("/{id}")
def inventory_by_id(id: int):
    print(id)
    item = inventory[id - 1]
    return item

@router.post("/")
def create_inventory(inventory_item: Inventory):
    inventory.append(inventory_item)
    return inventory_item

@router.put("/{id}")
def update_name(id: int, inventory_item: Inventory):
    inventory[id - 1].update(**inventory_item.dict())
    return { "message": f"The inventory {id} get update"}

@router.delete("/{id}")
def delete_inventory(id: int):
    item = inventory[id - 1]
    inventory.pop(id - 1)
    return { "message": f"The inventory {id} get delete"}