#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/13 14:23
# @Author : Srunkyo
# @File   : models.py
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)
from settings import CONNECTION_STRING
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(CONNECTION_STRING)


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ShoeTable(DeclarativeBase):
    __tablename__ = "shoe"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    # subtitle = Column('subtitle', String(200), nullable=True)
    price = Column('price', Float(), nullable=False)
    link = Column('link', Text(), nullable=True)
    # image_url = Column('image_url', Text(), nullable=True)
    source = Column('source', String(20), nullable=False)


row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

# Query the table
engine = db_connect()
create_table(engine)
Session = sessionmaker(bind=engine)
session = Session()
result = session.query(ShoeTable).all()
SHOE_DATA = [row2dict(row) for row in result]
SHOE_IDS = [d['id'] for d in SHOE_DATA]
SHOE_TITLES = [d['title'] for d in SHOE_DATA]
