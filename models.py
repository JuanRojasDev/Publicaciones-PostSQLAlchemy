from sqlalchemy import Boolean, Integer, Column, ForeignKey, String, Table, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field

Base = declarative_base()

metadata = MetaData()

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Integer)
    is_offer = Column(Boolean)
    orders = relationship("Order", secondary="order_items", back_populates="items")

    class PydanticConfig:
        orm_mode = True

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    phone = Column(String)
    orders = relationship("Order", back_populates="client")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client", back_populates="orders")
    items = relationship("Item", secondary="order_items", back_populates="orders")

    class PydanticConfig:
        orm_mode = True

class ItemInResponse(BaseModel):
    id: int
    name: str
    price: int
    is_offer: bool

    class Config:
        orm_mode = True
