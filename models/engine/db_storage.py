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
    """DBStorage
    """

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
        """all

        Args:
            cls (str, optional): name of the class. Defaults to None.

        Returns:
            dict: new dictionary of the information the query
        """
        query_obj = []
        if cls is not None:
            query_obj = self.__session.query(cls).all()
        else:
            list_class = [User, Place, State, City, Review, Amenity]
            for x in list_class:
                query_obj += self.__session.query(x).all()
        new_dict = {}
        for v in query_obj:
            id_class = type(v).__name__ + "." + v.id
            new_dict[id_class] = v
        return new_dict

    def new(self, obj):
        """new

        Args:
            obj (str):object at create
        """
        self.__session.add(obj)

    def save(self):
        """save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete

        Args:
            obj (str, optional): object at delete. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """reload
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """close
        """
        self.__session.remove()
