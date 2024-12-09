from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, RegisterSerializer

class RegisterUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        query_serializer=RegisterSerializer,
        security=[],
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message': 'Invalid data provided'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'User registered successfully'
        })


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self, *args):
        user_obj = self.get_object()
        serializer = UserSerializer(user_obj)
        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def patch(self, request):
        user_obj = self.get_object()
        serializer = UserSerializer(user_obj, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message': 'Invalid data'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'User details updated successfully'
        })

    def put(self, request):
        user_obj = self.get_object()
        serializer = UserSerializer(user_obj, data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message': 'Invalid data'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'User details fully updated successfully'
        })
