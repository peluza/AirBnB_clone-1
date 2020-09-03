#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from os import getenv


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
        cities = relationship("City", backref='state')
    else:
        @property
        def cities(self):
            """cities

            Returns:
                list: list of the information cities
            """
            obj = []
            ints = models.storage.all()
            for k, v in ints.items():
                if k.split(".")[0] == "City" and v.state_id == self.id:
                    obj.append(v)
            return obj
