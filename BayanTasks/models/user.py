from common.base_model import BayanBaseModel
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, Table, TIMESTAMP
from sqlalchemy.orm import relationship

association_table_user_team = Table('user_team', BayanBaseModel.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('team_id', Integer, ForeignKey('team.id'))
)

association_table_user_task = Table('user_task', BayanBaseModel.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)


class User(BayanBaseModel):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    name = Column(String(45))
    email = Column(String(45))
    type = Column(Enum('MANAGER', 'CUSTOMER'))
    encrypted_password = Column(String(45))
    user_salt = Column(String(45))

    user_address = relationship("UserAddress", viewonly=True)

    teams = relationship('Team',
                         secondary=association_table_user_team,
                         back_populates="users"
                         )

    tasks = relationship('Task',
                         secondary=association_table_user_task,
                         back_populates="users"
                         )


class UserAddress(BayanBaseModel):
    __tablename__ = 'user_address'
    __table_args__ = {'extend_existing': True}

    address = Column(String(255))
    longitude = Column(Float)
    latitude = Column(Float)

    user_id = Column(Integer, ForeignKey('user.id'))


class Team(BayanBaseModel):
    __tablename__ = 'team'
    __table_args__ = {'extend_existing': True}

    name = Column(String(45))
    tasks = relationship('Task')
    users = relationship(
        "User",
        secondary=association_table_user_team,
        back_populates="teams")


class Task(BayanBaseModel):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    tittle = Column(String(45))
    status = Column(Enum('ONPROGRESS', 'COMPLITED'))
    target = Column(Enum('USER', 'TEAM'))
    from_date = Column(TIMESTAMP)
    to_date = Column(TIMESTAMP)

    team_id = Column(Integer, ForeignKey('team.id'))
    users = relationship(
        "User",
        secondary=association_table_user_task,
        back_populates="tasks")
