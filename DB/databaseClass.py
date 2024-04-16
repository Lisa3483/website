from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Numeric, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from sqlalchemy import create_engine, MetaData

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    logged_in = Column(Boolean, default=False)
    datetime = Column(DateTime, default=func.now())
    balance = Column(Numeric(precision=10, scale=2), default=0.0)
    nickname = Column(String(10), nullable=False)
    hashed_password = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)


