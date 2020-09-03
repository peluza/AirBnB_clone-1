#!/usr/bin/python3
"""DBStorage
    """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        d_sql = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db)
        DBStorage.__engine = create_engine(d_sql, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        class_list = [User, State, City, Amenity, Place, Review]
        all_dict = {}
        if cls is not None:
            if type(cls) == str:
                class_obj = eval(cls)
            else:
                class_obj = cls
                cls = str(cls)
            for item in self.__session.query(class_obj):
                all_dict[cls + "." + item.id] = item
        else:
            for table in class_list:
                for item in self.__session.query(table):
                    all_dict[table.__class__.__name__ + "." + item.id] = item
        return all_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """call remove method"""
        self.__session.remove()
