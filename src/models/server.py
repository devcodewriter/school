from repository.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False) 

    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    admin_id = Column(Integer, ForeignKey('admins.id'))

    classroom = relationship("Classroom", back_populates="servers")
    admin = relationship("Admin", back_populates= "servers")

    # def __init__(self, id, name, classroom=None, admin=None):
    #     self.id = id
    #     self.name = name
    #     self.classroom = classroom
    #     self.admin = admin

    def __str__(self):
        return f"Server(id={self.id}, name={self.name}, admin={ self.admin.name if self.admin else "NULL" })"
    
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "classroom": self.classroom,
    #         "admin": self.admin
    #     }

    # @staticmethod
    # def from_dict(data):
    #     return Server(**data)