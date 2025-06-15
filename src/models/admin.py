from repository.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    servers = relationship("Server", back_populates="admin")

    # def __init__(self, id, name, servers=[]):
    #     self.id = id
    #     self.name = name
    #     self.servers = servers

    def __str__(self):
        return f"Admin(id={self.id}, name={self.name})"
    
    # def to_dict(self):
    #     return self.__dict__

    # @staticmethod
    # def from_dict(data):
    #     return Admin(**data)