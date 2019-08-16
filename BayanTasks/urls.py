from rest_framework import routers
from BayanTasks.views.user_controller import UserViewSet, UserRegistratonViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='user')
router.register(r'register', UserRegistratonViewset, base_name='registration')

urlpatterns = []

urlpatterns += router.urls
