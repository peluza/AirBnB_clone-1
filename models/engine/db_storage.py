#!/usr/bin/python3
"""DBStorage
    """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import MetaData
from sqlalchemy import (create_engine)


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
