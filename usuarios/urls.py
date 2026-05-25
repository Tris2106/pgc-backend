from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    RegisterView,
    ProfileView
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)

urlpatterns = router.urls + [

    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'perfil/',
        ProfileView.as_view(),
        name='perfil'
    ),
]