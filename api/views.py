from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from .tasks import send_welcome_email

# Public API
@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "Hello, this is a PUBLIC API!"})

# Protected API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({"message": "Hello, this is a PROTECTED API!", "user": serializer.data})

# Register API
@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Call Celery task!
        send_welcome_email.delay(user.email)
        return Response({"message": "User created! Email task started!"})
    return Response(serializer.errors, status=400)