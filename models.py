from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    userid = Column(String(5), unique=True)
    ext = Column(String(4), unique=True)

    def __init__(self, userid=None, ext=None):
        self.userid = userid
        self.ext = ext

    def __repr__(self):
        return '%r' % (self.ext)