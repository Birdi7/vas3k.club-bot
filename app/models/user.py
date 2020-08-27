from sqlalchemy import Column, String, Integer
from app.models.base import BaseModel, TimedMixin


class User(TimedMixin, BaseModel):
    secret_hash = Column(String)
    
    telegram_id = Column(Integer)
