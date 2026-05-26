from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


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

    try:
        
        user_obj = User.objects.filter(email=username_or_email).first()

        if user_obj:
            username = user_obj.username
        else:
            username = username_or_email

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Credenciales incorrectas"},
                status=400
            )

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

    except Exception as e:
        return Response({"error": str(e)}, status=500)