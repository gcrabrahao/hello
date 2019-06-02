from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    userid = Column(String(5), unique=True)
    extension = Column(String(4), unique=True)
    name = Column(String(100), unique=False)

    def __init__(self, userid=None, extension=None, name=None):
        self.userid = userid
        self.extension = extension
        self.name = name

    def __repr__(self):
        return '%r' % (self.ext)
