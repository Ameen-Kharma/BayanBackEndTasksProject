# from common.base_model import BayanBaseModel
# from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, TIMESTAMP
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import relationships
#
# from BayanTasks.models.user import association_table_user_task
#
#
# class Task(BayanBaseModel):
#     __tablename__ = 'user'
#
#     tittle = Column(String(45))
#     status = Column(Enum('ONPROGRESS', 'COMPLITED'))
#     target = Column(Enum('USER', 'TEAM'))
#     from_date = Column(TIMESTAMP)
#     to_date = Column(TIMESTAMP)
#
#     team_id = Column(Integer, ForeignKey('team.id'))
#     users = relationship(
#         "User",
#         secondary=association_table_user_task,
#         backref="tasks")
#
#
#
