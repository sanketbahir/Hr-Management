from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status, parsers
from drf_yasg.utils import swagger_auto_schema
from .models import Employee
from .serializers import EmployeeSerializer


@swagger_auto_schema(
    operation_summary="Employee Management API",
    request_body=EmployeeSerializer,
    security=[],
)
class EmployeeViewSet(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action == 'upload_image':
            return EmployeeImageSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload_image')
    def upload_image(self, request, pk=None):
        employee = self.get_object()
        serializer = self.get_serializer(employee, data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message': 'Invalid data'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'data': serializer.data,
            'message': 'Profile picture uploaded successfully'
        })

    def list(self, request):
        try:
            employees = Employee.objects.all()
            serializer = self.get_serializer(employees, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        except Exception:
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'errors': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Employee created successfully'
            })
        except Exception:
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def retrieve(self, request, pk=None):
        try:
            employee = self.get_object()
            serializer = self.get_serializer(employee)
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        except Exception:
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def update(self, request, pk=None):
        try:
            employee = self.get_object()
            serializer = self.get_serializer(employee, data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'errors': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Employee updated successfully'
            })
        except Exception:
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk=None):
        try:
            employee = self.get_object()
            employee.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Employee deleted successfully'
            })
        except Exception:
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
