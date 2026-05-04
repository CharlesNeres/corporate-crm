from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
