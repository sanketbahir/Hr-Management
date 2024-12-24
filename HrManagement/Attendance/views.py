from django.shortcuts import render
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
# from rest_framework.decorators import action

# Create your views here.
class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action =='list':
            return AttendanceSerializer
        if self.action == 'create':
            return AttendanceSerializer
        return self.serializer_class

#get all Attendance

    def list(self,request):
        try:
            Attendance_objs = Attendance.objects.all()
            serializer = self.get_serializer(Attendance_objs,many=True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#add Attendance
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
                'message':'Attendance Added successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#update all the fields of Attendance
    def update(self,request,pk=None):
        try:
            Attendance_objs = self.get_object()
            serializer = self.get_serializer(Attendance_objs,data=request.data,partial=False)
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
                'message':'Attendance updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#update specific field
    def partial_update(self,request,pk=None):
        try:
            Attendance_objs = self.get_object()
            serializer = self.get_serializer(Attendance_objs,data=request.data,partial=True)
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
                'message':'Attendance updated successefully'
            })
        except Exception as e:
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

#get single Attendance
    def retrive(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                Attendance_objs = Department.get_object()
                serializer = self.get_serializer(Attendance_objs)

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
            Attendance_objs = self.get_object()
            Attendance_objs.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Attendance deleted'
            })
        except Exception as e:
            raise({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })