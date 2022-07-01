from fastapi import FastAPI, status
from models import Todo
from database import engine
from sqlmodel import Session, select, SQLModel
from typing import List
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


@app.get("/", response_model=List[Todo], status_code=status.HTTP_200_OK)
async def get_todo():
    statement = select(Todo)
    results = session.exec(statement).all()
    return results


@app.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def post_todo(todo: Todo):
    new_todo = Todo(text=todo.text)
    session.add(new_todo)
    session.commit()
    return new_todo


@app.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    session = Session(bind=engine)
    statement = select(Todo).where(Todo.id == todo_id)
    to_do_dlt = session.exec(statement).one()
    session.delete(to_do_dlt)
    session.commit()
    return True


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
