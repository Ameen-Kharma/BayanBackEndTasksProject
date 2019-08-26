from BayanTasks.utils import AppSerializer
from BayanTasks.models.user import User, UserAddress, Task, Team
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

__author__ = 'AmeenKharma'


class UserAddressSerializer(AppSerializer):
    class Meta:
        model = UserAddress
        exclude = ('created', 'updated')


class TaskSerializer(AppSerializer):
    class Meta:
        model = Task
        exclude = ('created', 'updated')


class TeamSerializer(AppSerializer):
    class Meta:
        model = Team
        exclude = ('created', 'updated')


class UserSerializer(AppSerializer):
    class Meta:
        model = User
        exclude = ('encrypted_password', 'user_salt', 'created', 'updated')

    user_address = fields.Nested(UserAddressSerializer, many=True)
    teams = fields.Nested(TeamSerializer, many=True)
    tasks = fields.Nested(TaskSerializer, many=True)

