""" These classes define the ORM models to be used by sqlalchemy for the user database """

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class UserStatus(Base):
    __tablename__ = 'user_status'

    user_status_id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    STATUS_DICT = None
    STATUS_LIST = ["awaiting_confirmation", "email_confirmed","awaiting_approval","approved","denied"]

    @staticmethod
    def getStatus(statusName):
        if(UserStatus.STATUS_DICT == None):
            UserStatus.STATUS_DICT = {}
            # Pull status values out of DB
            for status in UserStatus.STATUS_LIST:
                UserStatus.STATUS_DICT[status] = UserStatus.setStatus(status)
        if(not statusName in UserStatus.STATUS_DICT):
            raise ValueError("Not a valid user status")
        return UserStatus.STATUS_DICT[statusName]

    @staticmethod
    def setStatus(name):
        """  Add id to dict for specified status, if not unique throw an exception

        Arguments:
        name -- Name of status to get an id for

        Returns:
        id of the specified status
        """
        # Create new session for this
        from dataactcore.models.userInterface import UserInterface
        UserStatus.session = UserInterface().Session()
        queryResult = UserStatus.session.query(UserStatus.user_status_id).filter(UserStatus.name==name).all()
        UserStatus.session.close()
        if(len(queryResult) != 1):
            # Did not get a unique result
            raise ValueError("Database does not contain a unique ID for type "+name)
        else:
            return queryResult[0].user_status_id

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(Text)
    email = Column(Text)
    name = Column(Text)
    agency = Column(Text)
    title = Column(Text)
    user_status_id = Column(Integer, ForeignKey("user_status.user_status_id"))
    status = relationship("UserStatus", uselist=False)

