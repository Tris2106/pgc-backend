from rest_framework.routers import DefaultRouter
from .views import CalendarioViewSet

router = DefaultRouter()

router.register(r'calendario', CalendarioViewSet)

urlpatterns = router.urls