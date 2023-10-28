import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String(250))
    description = Column(Text)
    gender = Column(String(250))
    height = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String(250))
    description = Column(Text)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    diameter = Column(Float)
    surface_water = Column(Integer)
    orbital_period = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String(250))
    description = Column(Text)
    model_name = Column(String(250))
    manufacturer = Column(String(250))
    price = Column(Float)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(Text)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime)
    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    def to_dict(self):
        return {}




# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
