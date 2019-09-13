from BayanTasks.models.user import User
from BayanTasks.common.libs.bayan_db import db_session
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from BayanTasks.utils.serializer import UserSerializer, TaskSerializer
from BayanTasks.utils.smart_response import smart_response
from BayanTasks.component.user_component import UserComponent


class UserViewSet(ViewSet):
    def __init__(self, **kwargs):
        pass

    def list(self, request):
        user = User(name="Ameen", email = "ameen123@ddaf.com", type='MANAGER', encrypted_password="ass",
                    user_salt="ass")
        db_session.add(user)
        db_session.commit()

    def retrieve(self, request, pk):
        return Response("success", 200)


class UserRegistratonViewset(ViewSet):

    # POST /register
    def create(self, request):
        request_data = request.data

        name = request_data.get("name", None)
        email = request_data.get('email', None)
        password = request_data.get('password')

        user = UserComponent.create_user(user_name=name, user_email=email, plain_password=password)
        user = UserComponent.login(request=request,  user_email=email, plain_password=password)
        try:
            result = UserSerializer().dump(user).data
        except Exception as e:
            print(str(e))
            return Response(str(e), status=200)

        return Response(result, status=200)


class UserLoginViewSet(ViewSet):
    def __init__(self, **kwargs):
        pass

    def create(self, request):
        request_data = request.data
        request_session = request.session
        name = request_data.get("name", None)
        email = request_data.get('email', None)
        password = request_data.get('password')

        user = UserComponent.login(request=request, user_email=email, plain_password=password)

        user = UserSerializer().dump(user).data
        return smart_response(user, 200)


class UserTaskViewSet(ViewSet):
    def __init__(self, **kwargs):
        pass

    def create(self, request, user_pk):
        logged_in_user_id = request.session.get("user_id")
        # Authorization.can_manage_user(logged_in_user_id=logged_in_user_id, user_id=user_pk)
        request_data = request.data
        task_from = request_data.get('from')
        task_to = request_data.get('task_to')
        task_title = request_data.get('title')
        task_description = request_data.get('description')
        UserComponent.create_user_task(task_from=task_from, task_to=task_to, task_title=task_title,
                                       task_description=task_description)

    def list(self, request, user_pk):
        request_session = request.session

        logged_in_user_id = request.session.get("user_id")
        # Authorization.can_manage_user(logged_in_user_id=logged_in_user_id, user_id=user_pk)
        tasks = UserComponent.get_task_by_user_id(user_pk)

        tasks = TaskSerializer(many=True).dump(tasks).data
        return smart_response(tasks, 200)

    def retrieve(self, request, user_pk, pk):
        return Response("success", 200)

