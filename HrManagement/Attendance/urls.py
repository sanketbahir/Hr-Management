from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet

router =DefaultRouter()
router.register('',AttendanceViewSet,basename='Attendance')
app_name = 'Attendance'

urlpatterns = [
    path('',include(router.urls))
]