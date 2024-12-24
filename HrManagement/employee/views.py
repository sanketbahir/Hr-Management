from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action


# Create your views here.
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action =='list':
            return EmployeeSerializer
        if self.action == 'create':
            return EmployeeSerializer
        return self.serializer_class

#get all Employee

    def list(self,request):
        try:
            Employee_objs = Employee.objects.all()
            serializer = self.get_serializer(Employee_objs,many=True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#add Employee
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
                'message':'Employee Added successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#update all the fields of Employee
    def update(self,request,pk=None):
        try:
            Employee_objs = self.get_object()
            serializer = self.get_serializer(Employee_objs,data=request.data,partial=False)
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
                'message':'Employee updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
#update specific field
    def partial_update(self,request,pk=None):
        try:
            Employee_objs = self.get_object()
            serializer = self.get_serializer(Employee_objs,data=request.data,partial=True)
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
                'message':'Employee updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#get single Employee
    def retrive(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                Employee_objs = Employee.get_object()
                serializer = self.get_serializer(Employee_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#delete Employee
    def destroy(self,request,pk=None):
        try:
            id = pk #1
            Employee_objs = self.get_object()
            Employee_objs.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Employee deleted'
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })