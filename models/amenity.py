#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """The Amenity table. This table establishes a
    many-to-many relationship between Place and Amenity
    through the place-amenities attribute.
    """
    __tablename__ = 'amenities'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False,
                                   back_populates="amenities")
