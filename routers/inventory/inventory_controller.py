from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.inventory.inventory_model import DbInventory, InventoryBase


def create_inventory(db: Session, request: InventoryBase):
    new_inventory = DbInventory(
        description=request.description, price=request.price, stock=request.stock
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def get_all_inventory(db: Session):
    return db.query(DbInventory).all()


def get_inventory_by_id(db: Session, inventory_id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    return inventory


def update_inventory(db: Session, inventory_id: int, request: InventoryBase):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    inventory.description = request.description
    inventory.price = request.price
    inventory.stock = request.stock
    db.commit()
    db.refresh(inventory)
    return inventory


def deleted_inventory(db: Session, inventory_id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == inventory_id).first()
    db.delete(inventory)
    db.commit()
    return JSONResponse(
        content={"detail": f"Inventory id {inventory_id} deleted successful!"}
    )
