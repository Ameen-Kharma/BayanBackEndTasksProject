from rest_framework import routers
from BayanTasks.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
#router.register(r'register')

urlpatterns = []

urlpatterns+= router.urls