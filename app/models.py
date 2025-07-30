from sqlalchemy import Column, Integer, String
from . import db

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
