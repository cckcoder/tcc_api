from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func

from models.database import Base

from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class DbInventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    price = Column(DECIMAL)
    stock = Column(Integer)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now()
    )

class InventoryDisplayBase(BaseModel):
    id: int
    description: Optional[str] = ""
    price: Decimal
    stock: int
    created_date: datetime
    updated_date: datetime

class InventoryBase(BaseModel):
    description: str
    price: Decimal
    stock: int