from rest_framework_nested import routers

from BayanTasks.views.user_controller import UserViewSet, UserRegistratonViewset, UserLoginViewSet, UserTaskViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='user')
router.register(r'register', UserRegistratonViewset, base_name='registration')
router.register(r'login', UserLoginViewSet, base_name='login')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user', trailing_slash=False)

users_router.register('tasks', UserTaskViewSet, base_name='task')
urlpatterns = []

urlpatterns += router.urls + users_router.urls
