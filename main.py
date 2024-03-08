from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ItemBase(BaseModel):
    id : int
    name: str
    price: int
    is_offer: bool = None

class ClientBase(BaseModel):
    id : int
    name: str
    phone: str

class OrderBase(BaseModel):
    id : int
    client: ClientBase
    items: List[ItemBase]

# CONEXION
    
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/order/")
async def create_order(order: OrderBase, db: db_dependency):
        # Verifica si el cliente existe en la base de datos
        db_client = db.query(models.Client).filter_by(id=order.client.id).first()

        if not db_client:
            # Si el cliente no existe, crea uno nuevo
            db_client = models.Client(name=order.client.name, phone=order.client.phone)
            db.add(db_client)
            db.commit()
            db.refresh(db_client)

        # Verifica si los items existen en la base de datos
        db_items = []
        for item in order.items:
            db_item = db.query(models.Item).filter_by(id=item.id).first()
            if not db_item:
                # Si el item no existe, crea uno nuevo
                db_item = models.Item(name=item.name, price=item.price)
                db.add(db_item)
                db.commit()
                db.refresh(db_item)
            db_items.append(db_item)

        # Crea la nueva orden asociada con el cliente y los items
        db_order = models.Order(client_id=db_client.id, items=db_items)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        return db_order
    