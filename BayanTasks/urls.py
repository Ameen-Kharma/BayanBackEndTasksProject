from rest_framework import routers
from BayanTasks.views.user_controller import UserViewSet, UserRegistratonViewset, UserLoginViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='user')
router.register(r'register', UserRegistratonViewset, base_name='registration')
router.register(r'login', UserLoginViewSet, base_name='login')

urlpatterns = []

urlpatterns += router.urls
