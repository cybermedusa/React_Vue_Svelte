from cmath import log
from os import stat
from fastapi import Depends, FastAPI, status, HTTPException
from models import ToDo
from database import engine
from sqlmodel import Session, select, SQLModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


def create_db():
    SQLModel.metadata.create_all(engine)


session = Session(bind=engine)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db()


@app.get("/", response_model=List[ToDo], status_code=status.HTTP_200_OK)
async def get_todo():
    statement = select(ToDo)
    results = session.exec(statement).all()
    return results


@app.post("/", response_model=ToDo, status_code=status.HTTP_201_CREATED)
async def post_todo(todo: ToDo):
    new_todo = ToDo(text=todo.text)
    session.add(new_todo)
    session.commit()
    return new_todo


@app.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    session = Session(bind=engine)
    statement = select(ToDo).where(ToDo.id == todo_id)
    to_do_dlt = session.exec(statement).one()
    session.delete(to_do_dlt)
    session.commit()
    return True
