#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DB
    cities = relationship(
        'City',
        back_populates='state',
        cascade='all, delete-orphan'
        )

    # @property
    # def cities(self):
    #     """ returns the list of City instances with
    #     state_id equals to the current State.id"""
    #     cities_dict = storage.all('City')
    #     return cities_dict.values()
