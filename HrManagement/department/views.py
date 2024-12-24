from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action


# Create your views here.
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action =='list':
            return DepartmentSerializer
        if self.action == 'create':
            return DepartmentSerializer
        return self.serializer_class

#get all Department

    def list(self,request):
        try:
            Department_objs = Department.objects.all()
            serializer = self.get_serializer(Department_objs,many=True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#add Department
#request.data = data sent by the client to http request body
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data) #Kasturi
            if not serializer.is_valid(): #False
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data, #Kasturi
                'message':'Department Added successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#update all the fields of Department
    def update(self,request,pk=None):
        try:
            Department_objs = self.get_object()
            serializer = self.get_serializer(Department_objs,data=request.data,partial=False)
            if not serializer.is_valid():
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Department updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#update specific field
    def partial_update(self,request,pk=None):
        try:
            Department_objs = self.get_object()
            serializer = self.get_serializer(Department_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Department updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#get single Department
    def retrive(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                Department_objs = Department.get_object()
                serializer = self.get_serializer(Department_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#delete Department
    def destroy(self,request,pk=None):
        try:
            id = pk #1
            Department_objs = self.get_object()
            Department_objs.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Department deleted'
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })