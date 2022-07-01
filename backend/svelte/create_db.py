from sqlmodel import SQLModel
from models import ToDo
from database import engine

SQLModel.metadata.create_all(engine)
