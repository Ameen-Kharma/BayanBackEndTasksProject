from BayanTasks.models.user import User
from common.libs.bayan_db import db_session
from rest_framework.viewsets import ViewSet


class UserViewSet(ViewSet):
    def __init__(self,**kwargs):
        pass

    def list(self, request):
        user = User(name="Ameen", email = "ameen123@ddaf.com", type='MANAGER', encrypted_password="ass",
                    user_salt="ass")
        db_session.add(user)
        db_session.commit()
