from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

__author__ = 'AmeenKharma'


class AppSerializer(ModelSchema):
    created = fields.DateTime(format="%b %d, %Y %H:%M:%S GMT", attribute="created")
    updated = fields.DateTime(format="%b %d, %Y %H:%M:%S GMT", attribute="updated")
