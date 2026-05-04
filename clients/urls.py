from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
