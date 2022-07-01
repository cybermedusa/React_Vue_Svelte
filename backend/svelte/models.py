from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class ToDo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
