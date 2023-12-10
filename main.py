import models

from datetime import date
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Item(BaseModel):
    name: str
    model: str
    serial_no: str
    cost: float
    purchase_date: date


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Create an item
@app.post("/item")
async def create_item(item: Item, db: Session = Depends(get_db)):
    item_obj = models.Items()
    item_obj.name = item.name
    item_obj.model = item.model
    item_obj.serial_no = item.serial_no
    item_obj.cost = item.cost
    item_obj.purchase_date = item.purchase_date

    db.add(item_obj)
    db.commit()

    return {"message": "Item has been added."}

