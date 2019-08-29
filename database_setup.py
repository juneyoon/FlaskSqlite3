import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Cooking(Base):
    __tablename__ = 'cooking'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id' : self.id,
            'name' : self.name
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    cooking_id = Column(Integer, ForeignKey('cooking.id'))
    cooking = relationship(Cooking)

    @property
    def serialize(self):
        return{
            'name' : self.name,
            'id' : self.id,
            'description' : self.description,
        }

engine = create_engine('sqlite:///cookingmenu.db')

Base.metadata.create_all(engine)
#4. SERVERS, ~CRUD LESSON 1 working with CRUD
#https://classroom.udacity.com/nanodegrees/nd004/parts/4dcefa2a-fb54-4909-9708-9ef2839e5340/modules/349fd477-16d6-44ae-b33a-2b8521735718/lessons/3621198668/concepts/36123887380923

