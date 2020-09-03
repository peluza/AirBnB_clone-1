#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
from models.city import City
from models.user import User
from  os import getenv
import models

metadata = Base.metadata

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'), nullable=False),
        Column(
            'amenity_id',
            String(60), ForeignKey('amenities.id'), nullable=False),
    )
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place')
        amenities = relationship(
            "Amenity",
            secondary=place_amenity, viewonly=False,
            back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """reviews

            Returns:
                list: list of the instance
            """
            obj_l = []
            ints = models.storage.all()
            for k, v in ints.items():
                if k.split(".")[0] == "Review" and v.place_id == self.id:
                    obj_l.append(v)
            return obj_l

        @property
        def amenities(self):
            """amenities

            Returns:
                list: list of the instance
            """
            obj_l = []
            ints = models.storage.all()
            for k, v in ints.items():
                if k.split(".")[0] == "Amenity" and\
                        k.split(".")[1] in self.amenity_ids:
                    obj_l.append(v)
            return obj_l

        @amenities.setter
        def amenities(self, value):
            """amenities

            Args:
                value (uuid): id 
            """
            if value.__class__.__name__ == "Amenity":
                self.amenity_ids.append(value.id)
