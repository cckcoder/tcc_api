from sqlalchemy import Column
from sqlalchemy.sql.sqltype import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func

from models.database import Base


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
        onupdcate=func.now()
    )