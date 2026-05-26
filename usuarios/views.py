from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


@api_view(['POST'])
def login_view(request):

    username = request.data.get('username')
    password = request.data.get('password')

    try:
        
        user_obj = User.objects.filter(email=username).first()

        if user_obj:
            username = user_obj.username

        user = authenticate(username=username, password=password)

        if user is not None:
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

        return Response({"error": "Credenciales incorrectas"}, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)