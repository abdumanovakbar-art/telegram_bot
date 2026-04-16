from sqlalchemy import Column, Integer, BIGINT, create_engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session

engine = create_engine('postgresql+psycopg2://postgres:1@localhost/queuemaster')
session = Session(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = Column(Integer, primary_key=True)
    telegram_id : Mapped[int] = Column(BIGINT , unique=True)
    name : Mapped[str]

class Category(Base):
    id : Mapped[int] = Column(Integer, primary_key=True)
    name : Mapped[str]


class Task(Base):
    id : Mapped[int] = Column(Integer, primary_key=True)
    user_id : Mapped[int] = Column(ForeignKey('users.telegram_id'))
    category_id : Mapped[int] = Column(ForeignKey('categories.id'))
    title : Mapped[str]
    description : Mapped[str] = Column(String)
    status : Mapped[bool]







    #
    # user_id: Mapped[int] = mapped_column(BigInteger,ForeignKey("userss.tg_id"))
