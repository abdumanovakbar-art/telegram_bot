from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import engine, User


def get_user(tg_id):
    with Session(engine) as session:
        user = session.execute(
            select(User).where(User.telegram_id == tg_id)
        ).scalar()
        return user


def save_user(tg_id, name , age):
    with Session(engine) as session:
        user = session.execute(
            select(User).where(User.telegram_id == tg_id)
        ).scalar_one_or_none()
        if not user:
            new_user = User(telegram_id=tg_id, name=name , age=age)
            session.add(new_user)
            session.commit()
            return new_user

        return user