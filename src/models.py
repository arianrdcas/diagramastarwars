import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    iduser = Column(Integer, primary_key=True)
    nameuser = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    emailuser = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    idplaneta = Column(Integer, primary_key=True)
    nameplaneta = Column(String(250))

class Planetafavorito(Base):
    __tablename__ = 'planetafavorito'
    idplanetafavorito = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.iduser'))  
    id_planet = Column(Integer, ForeignKey('planeta.idplaneta'))
    planeta = relationship(Planeta)
    user = relationship(User)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    idpersonaje = Column(Integer, primary_key=True)
    namepersonaje = Column(String(250))
    nameactor = Column(String(250))

class Personajefavorito(Base):
    __tablename__ = 'personajefavorito'
    idpersonajefavorito = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.iduser'))  
    id_personaje = Column(Integer, ForeignKey('personaje.idpersonaje'))
    personaje = relationship(Personaje)
    user = relationship(User)

class Nave(Base):
    __tablename__ = 'nave'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    idnave = Column(Integer, primary_key=True)
    namenave = Column(String(250))

class Navefavorito(Base):
    __tablename__ = 'navefavorito'
    idnavefavorito = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.iduser'))  
    id_nave = Column(Integer, ForeignKey('nave.idnave'))
    nave = relationship(Nave)
    user = relationship(User)

class Episodio(Base):
    __tablename__ = 'episodio'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    idepisodio = Column(Integer, primary_key=True)
    nameepisodio = Column(String(250))  
    annoepisodio = Column(Integer) 

class Episodiopersonaje(Base):
    __tablename__ = 'episodiopersonaje'
    idepisodiopersonaje = Column(Integer, primary_key=True)
    id_episodio = Column(Integer, ForeignKey('episodio.idepisodio'))  
    id_personaje = Column(Integer, ForeignKey('personaje.idpersonaje'))
    episodio = relationship(Episodio)
    personaje = relationship(Personaje)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')