from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

    @classmethod
    def add_admin_user(cls, session):
        admin_user = cls(id=1, username="admin", password="god")
        session.add(admin_user)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()

    @classmethod
    def check_credentials(cls, session, username, password):
        try:
            user = (
                session.query(cls).filter_by(username=username, password=password).one()
            )
            return True
        except NoResultFound:
            return False

    @classmethod
    def get_user_id_by_credentials(cls, session, username, password):
        try:
            user = (
                session.query(cls).filter_by(username=username, password=password).one()
            )
            return user.id
        except NoResultFound:
            return None