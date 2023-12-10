from datetime import datetime
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, Date, Float
from database import Base


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    model = Column(String)
    serial_no = Column(String)
    cost = Column(Float)
    purchase_date = Column(Date)

