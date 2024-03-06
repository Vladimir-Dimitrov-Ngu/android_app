from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_PATH
from models import MlBase, Models, Money, MoneyBase, User, UserBase

engine = create_engine(DB_PATH)

UserBase.metadata.create_all(engine)
MoneyBase.metadata.create_all(engine)
MlBase.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

User.add_admin_user(session)
Money.add_money_admin(session)
Models.add_all_models(session)
# print(User.check_credentials(session, username='admin', password='god'))

session.close()
