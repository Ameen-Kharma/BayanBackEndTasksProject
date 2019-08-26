from common.base_model import BayanBaseModel
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, Table, TIMESTAMP
from sqlalchemy.orm import relationship

# class UserTask(BayanBaseModel):
#     __tablename__ = 'user_task'
#     __table_args__ = {'extend_existing': True}
#
#     user_id = Column(
#       Integer,
#       ForeignKey('user.id'),
#       primary_key=True)
#
#     task_id = Column(
#        Integer,
#        ForeignKey('task.id'),
#        primary_key=True)


class User(BayanBaseModel):
    __tablename__ = 'user'

    name = Column(String(45))
    email = Column(String(45))
    type = Column(Enum('MANAGER', 'CUSTOMER'))
    encrypted_password = Column(String(45))
    user_salt = Column(String(45))

    user_address = relationship("UserAddress")

    teams = relationship('Team', uselist=True)

    tasks = relationship('Task', uselist=True)


class UserAddress(BayanBaseModel):
    __tablename__ = 'user_address'

    address = Column(String(255))
    longitude = Column(Float)
    latitude = Column(Float)

    user_id = Column(Integer, ForeignKey('user.id'))


class Team(BayanBaseModel):
    __tablename__ = 'team'

    name = Column(String(45))
    tasks = relationship('Task')
    user_id = Column(Integer, ForeignKey('user.id'))


class Task(BayanBaseModel):
    __tablename__ = 'task'

    tittle = Column(String(45))
    status = Column(Enum('ONPROGRESS', 'COMPLITED'))
    target = Column(Enum('USER', 'TEAM'))
    from_date = Column(TIMESTAMP)
    to_date = Column(TIMESTAMP)

    team_id = Column(Integer, ForeignKey('team.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

