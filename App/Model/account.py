from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from App.Data.database import Base
from App.Data.database import Sessionlocal
import uuid
from App.Data.mixins import Timestamp
from dataclasses import dataclass
def create_uuid():
    return 


class Accounts(Timestamp, Base):
    __tablename__ = "Accounts"
    id = Column(Integer, primary_key=True,)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_joiend = Column(DateTime)
    profile = relationship("Profile",  back_populates="owner", uselist= False)

  
    def get_name(self):
        return self.username
  

    def dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "date_joiend": self.date_joiend,
            
        }
        
class Profile(Timestamp, Base):
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    frist_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_data = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)
    apartment_number = Column(Integer, nullable=False)
    zip = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    profile_pictor = Column(String, nullable=False)
    avatar = Column(String, nullable=False)
    bio = Column(String, nullable=False)
    profile_id = Column(Integer, ForeignKey("Accounts.id"), nullable=False)
    owner = relationship("Accounts",  back_populates="profile")

    def dict(self):
        return {
            "id": self.id,
            "frist_name": self.frist_name,
            "last_name": self.last_name,
            "birth_data": self.birth_data,
            "address": self.address,
            "apartment_numbe": self.apartment_number,
            "zip": self.zip,
            "city": self.city,
            "profile_pictor": self.profile_pictor,
            "avatar": self.avatar,
            "bio": self.bio,
        }


# class Connections(Base):
#     __tablename__           = "Connections"
#     id                      = Column(Integer, primary_key=True)
#     sender_id               = Column(Integer, primary_key=True)
#     receiver_id             = Column(Integer, primary_key=True)
#     connections_id          = Column(Integer, ForeignKey("Accounts.id"), nullable=False)
#     connections_owner       = relationship("Accounts",  back_populates="connections")

# class Circle(Base):

#     name                    =
#     description             =
#     creator_id              =
#     members                 =
#     image                   =

# class Message(Base):

#     sender_id               =
#     receiver_id             =
#     message                 =

# class Post(Base):
#     circle_id               =
#     user_id                 =
#     date                    =
#     time                    =

# class Reaction(Base):

#     post_id                  =
#     user_id                  =
#     type                     =

# class Comment(Base):

#     post_id                  =
#     user_id                  =
#     content                  =
#     date                     =
#     time                     =