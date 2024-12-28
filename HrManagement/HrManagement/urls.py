"""HrManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from drf_yasg.utils import swagger_auto_schema

schema_view = get_schema_view(
   openapi.Info(
      title="HrManagement API",
      default_version='v1',
      description="HrManagement API Management",
      terms_of_service="https://127.0.0.1:8000",
      contact=openapi.Contact(email="sanketbahir2016@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    authentication_classes=(authentication.JWTAuthentication,),
#    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('departmnt/',include('department.urls')),
    path('Attendance/',include('Attendance.urls')),
<<<<<<< HEAD
    path('employee/',include('employee.urls')),
    path('user/',include('user.urls')),
    path('api/token/', swagger_auto_schema(methods=['post'],security=[])(TokenObtainPairView.as_view())),
    path('api/token/refresh/',swagger_auto_schema(methods=['post'],security=[])(TokenRefreshView.as_view())),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        	
=======
    
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        	

<<<<<<< HEAD

          
=======
    ]       
>>>>>>> suchitra
>>>>>>> fd6d0b8c5e27194f5f4161022f1ccf50c9d23821
