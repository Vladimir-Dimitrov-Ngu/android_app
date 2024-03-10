from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Money(Base):
    __tablename__ = "money"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True)
    money = Column(Integer)

    @classmethod
    def add_money_admin(cls, session):
        money_for_admin = cls(username="admin", money=500)
        session.add(money_for_admin)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()

    @classmethod
    def get_money_by_username(cls, session, username):
        try:
            money = session.query(cls).filter_by(username=username).one()
            return money.money
        except NoResultFound:
            return None

    @classmethod
    def add_money_by_username(cls, session, username, amount=100):
        try:
            user_money = session.query(cls).filter_by(username=username).one()
            user_money.money += amount
            session.commit()
            return None
        except NoResultFound:
            return None
