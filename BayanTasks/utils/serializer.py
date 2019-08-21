# from BayanTasks.utils import AppSerializer
from BayanTasks.models.user import User, UserAddress

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

__author__ = 'AmeenKharma'


class AppSerializer(ModelSchema):
    created = fields.DateTime(format="%b %d, %Y %H:%M:%S GMT", attribute="created")
    updated = fields.DateTime(format="%b %d, %Y %H:%M:%S GMT", attribute="updated")


class UserAddressSerializer(AppSerializer):
    class Meta:
        model = UserAddress
        exclude = ('created', 'updated')


class UserSerializer(AppSerializer):
    class Meta:
        model = User
        #exclude = ('encrypted_password', 'user_salt', 'created', 'updated', 'teams', 'tasks')

    user_address = fields.Nested(UserAddressSerializer, many=False)

