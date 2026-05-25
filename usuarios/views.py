from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import Usuario

from .serializers import (
    UsuarioSerializer,
    RegisterSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = RegisterSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user