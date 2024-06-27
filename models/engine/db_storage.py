#!/usr/bin/python3
"""This class is a new storage environment, using
MySQLAlchemy to interact with the database.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialization method"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST') or 'localhost'
        db = os.getenv('HBNB_MYSQL_DB')
        connection_string = f'mysql+mysqldb://{user}:{pwd}@{host}/{db}'
        self.__engine = create_engine(connection_string, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            for table in reversed(metadata.sorted_tables):
                self.__engine.execute(table.drop(self.__engine))

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """This method queries the database for all objects
        of a certain class.
        """
        results = {}
        if cls is not None:
            query1 = self.__session.query(cls).all()
            for obj in query1:
                key = type(obj).__name__ + "." + str(obj.id)
                results[key] = obj

        else:
            list_obj = [User, State, City, Amenity, Place, Review]
            for cls in list_obj:
                query2 = self.__session.query(cls).all()
                for obj in query2:
                    key = type(obj).__name__ + "." + str(obj.id)
                    results[key] = obj
        return results

    def new(self, obj):
        """This method adds an object to the database session"""
        self.__session.add(obj)

    def save(self):
        """This method commits all changes of the current database
        session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes an object from the current
        database session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This method creates all tables in the database,
        creates the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
