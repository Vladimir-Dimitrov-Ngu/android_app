from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Models(Base):
    __tablename__ = "models"
    id = Column(Integer, Sequence("models_id"), primary_key=True)
    model_name = Column(String(100))
    short_name = Column(String(50))

    @classmethod
    def add_all_models(cls, session):
        models = [
            cls(id=1, model_name="logistic regression", short_name="lr"),
            cls(id=2, model_name="decision tree", short_name="dt"),
            cls(id=3, model_name="catboost", short_name="ct"),
        ]

        session.add_all(models)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
