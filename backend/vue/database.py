from sqlmodel import Session, SQLModel, create_engine, text


sqlite_url = "sqlite:///./sql_app.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
