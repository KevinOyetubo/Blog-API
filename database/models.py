from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey, Unicode
from .database import Base
import datetime
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'Blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created = Column(DATETIME, default=datetime.datetime.now())
    publisher_id = Column(Integer, ForeignKey("users.id"))


    author = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
   
    blogs = relationship("Blog", back_populates="author")