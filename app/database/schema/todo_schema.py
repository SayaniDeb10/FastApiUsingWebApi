from sqlalchemy import Column , Integer, String, VARCHAR
from ..db import Base

class TodoSchema(Base):
    __tablename__ = "todos"