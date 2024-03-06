import jwt
from backend.config import SECRET_KEY, USER_PASSWORD
from backend.database.config import DB_PATH
from backend.models import User
from backend.database.models import Money as MoneyDB
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
session = Session()


def money(user: User):
    money = MoneyDB.get_money_by_username(session, user.username)
    return {"money": money}
