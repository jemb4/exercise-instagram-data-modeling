import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(120), nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('User.ID'))
    url = Column(String)

class Follower(Base):
    __tablename__ = 'Follower'
    ID = Column(Integer, primary_key=True)
    user_from_ID = Column(Integer, ForeignKey('User.ID'))
    user_to_ID = Column(Integer, ForeignKey('User.ID'))

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    post_ID = Column(Integer, ForeignKey('Post.ID'))
    author_ID = Column(Integer, ForeignKey('User.ID'))

class Private_msg(Base):
    __tablename__ = 'Private_msg'
    ID = Column(Integer, primary_key=True)
    private_msg = Column(String, nullable=False)
    user_from_ID = Column(Integer, ForeignKey('User.ID'))
    user_to_ID = Column(Integer, ForeignKey('User.ID'))

class Saved_post(Base):
    __tablename__ = "Saved_post"
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('Post.ID'))

class Fav_comment(Base):
    __tablename__ = "Fav_comment"
    ID = Column(Integer, primary_key=True)
    comment_ID = Column(Integer, ForeignKey('Comment.ID'))



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e