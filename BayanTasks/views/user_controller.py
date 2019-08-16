from BayanTasks.models.user import User
from common.libs.bayan_db import db_session
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from BayanTasks.component.user_component import UserComponent


class UserViewSet(ViewSet):
    def __init__(self,**kwargs):
        pass

    def list(self, request):
        user = User(name="Ameen", email = "ameen123@ddaf.com", type='MANAGER', encrypted_password="ass",
                    user_salt="ass")
        db_session.add(user)
        db_session.commit()


class UserRegistratonViewset(ViewSet):


    def create(self, request):
        request_data = request.data

        name = request_data.get("name", None)
        email = request_data.get('email', None)
        password = request_data.get('password')

        UserComponent.create_user(user_name=name, user_email=email, plain_password=password)
        return Response({"MESSAGE": 'SUCCESSFULLY'}, status=200)
