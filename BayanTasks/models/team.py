from common.base_model import BayanBaseModel
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship

from BayanTasks.models.user import association_table_user_team


class Team(BayanBaseModel):
    __tablename__ = 'team'

    name = Column(String(45))
    tasks = relationship('Task')
    users = relationship(
        "User",
        secondary=association_table_user_team,
        back_populates="tasks")






