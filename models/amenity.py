#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from os import getenv


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place",
        # secondary="places", back_populates="place_amenity", )
    else:
        name = ""
