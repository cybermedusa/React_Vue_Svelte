from sqlmodel import SQLModel
from models import Todo
from database import engine

SQLModel.metadata.create_all(engine)
