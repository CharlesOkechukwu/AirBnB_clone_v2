#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0.0)
        longitude = Column(Integer, nullable=False, default=0.0)
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship(
            'Review',
            back_populates='place',
            cascade='all, delete-orphan'
            )
    # place_amenity = relationship("Amenity", secondary=
    # "amenities", back_populates="place_amenities", )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id. It will be the FileStorage
            relationship between Place and Review
            """
            all_reviews = models.storage.all('Review').values()
            relation = []
            for review in all_reviews:
                if review.place_id == self.id:
                    relation.append(review)
            return relation
