from sqlalchemy.orm import Session

from models.inventory.inventory_model import DbInventory, InventoryBase


def create_inventory(db: Session, request: InventoryBase):
    new_inventory = DbInventory(
        description=request.description,
        price=request.price,
        stock=request.stock
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def get_all_inventory(db: Session):
    return db.query(DbInventory).all()