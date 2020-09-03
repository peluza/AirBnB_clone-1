#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from os import getenv
import models


class State(BaseModel, Base):
    """State

    Args:
        BaseModel (cls): BaseModel
        Base (cls): Base

    Returns:
        list: list of the information cities
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref='state', cascade="all, delete")
    else:
        @property
        def cities(self):
            """cities

            Returns:
                list: list of the information cities
            """
            obj = []
            ints = models.storage.all(City)
            for v in ints.values():
                if v.state_id == self.id:
                    obj.append(v)
            return obj
