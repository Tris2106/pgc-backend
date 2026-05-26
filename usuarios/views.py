from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Usuario
from .serializers import UsuarioSerializer, RegisterSerializer


# -------------------------
# CRUD Usuario
# -------------------------
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# -------------------------
# REGISTER
# -------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Usuario creado correctamente",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            })

        return Response(serializer.errors, status=400)


# -------------------------
# PROFILE
# -------------------------
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })


# -------------------------
# LOGIN
# -------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username_or_email = request.data.get('username')
    password = request.data.get('password')

    if not username_or_email or not password:
        return Response(
            {"error": "Username/email y password son requeridos"},
            status=400
        )

    user_obj = User.objects.filter(email=username_or_email).first()

    username = user_obj.username if user_obj else username_or_email

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Credenciales incorrectas"}, status=400)

    refresh = RefreshToken.for_user(user)

    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    })