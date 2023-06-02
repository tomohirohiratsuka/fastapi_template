from sqlalchemy import Column, Integer, String

from database import Base

from .mixins import TimestampMixin


class Sample(Base, TimestampMixin):
    __tablename__ = "samples"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True)
    age = Column(Integer)
    email = Column(String(255))
