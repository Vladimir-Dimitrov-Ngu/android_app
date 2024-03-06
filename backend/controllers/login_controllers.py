import jwt
from backend.config import SECRET_KEY, USER_PASSWORD
from backend.database.config import DB_PATH
from backend.models import User
from backend.database.models import User as UserDB
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
session = Session()

def login(user: User):
    token = create_token(user.username, user.password)
    return {"access_token": token}


def create_token(username: str, password: str):
    if UserDB.check_credentials(session, username=username, password=password):
    #if username in USER_PASSWORD and USER_PASSWORD[username] == password:
        token_payload = {"username": username, "password": password}
        token = jwt.encode(token_payload, SECRET_KEY)
        return token
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")