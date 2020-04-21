import sqlite3
import sys
# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base
# for creating foreign key relationshiop between the tables
from sqlalchemy.orm import relationship
# for configuration
from sqlalchemy import create_engine

# create declarative base instance
Base = declarative_base()

# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///books-collection.db')

Base.metadata.create_all(engine)

# we create the class Book and extend it from the Base Class.


class Book(Base):
    __tablename__ = 'book'

    # primary key identifies each row uniquely
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)  # required when nullable=False
    author = Column(String(250), nullable=False)
    genre = Column(String(250))
