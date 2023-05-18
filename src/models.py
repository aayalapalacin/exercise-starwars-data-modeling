import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"),primary_key=True),
    Column("planet_id", ForeignKey("planets.id"),primary_key=True),
)
favorite_characters = Table(
    "favorite_characters",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"),primary_key=True),
    Column("character_id", ForeignKey("characters.id"),primary_key=True),
)
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    favorite_planets = relationship("Planets",secondary=favorite_planets,lazy="subquery",backref="user")
    favorite_characters = relationship("Characters",secondary=favorite_characters,lazy="subquery",backref="user")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def to_dict(self):
        return {}
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
