from sqlalchemy import Column, Integer, BIGINT, create_engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session
from sqlalchemy.testing.schema import mapped_column

engine = create_engine('postgresql+psycopg2://postgres:1@host.docker.internal:5432/postgres')
# postgresql+psycopg2://postgres:1@localhost/postgres
session = Session(engine)
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id : Mapped[int] = mapped_column(BIGINT , unique=True)
    name : Mapped[str]
    age : Mapped[int]

class Category(Base):
    __tablename__ = 'categories'
    id : Mapped[int] = Column(Integer, primary_key=True)
    name : Mapped[str]

class Task(Base):
    __tablename__ = 'tasks'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(BIGINT , ForeignKey('users.telegram_id'))
    category_id : Mapped[int] = mapped_column(ForeignKey('categories.id'))
    title : Mapped[str]
    description : Mapped[str] = Column(String)
    status : Mapped[bool]

Base.metadata.create_all(engine)