from rest_framework.routers import DefaultRouter
from .views import (
    TareaViewSet,
    CategoriaViewSet,
    RecordatorioViewSet
)

router = DefaultRouter()

router.register(r'tareas', TareaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'recordatorios', RecordatorioViewSet)

urlpatterns = router.urls