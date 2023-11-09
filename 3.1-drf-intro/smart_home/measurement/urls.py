from django.urls import path

from measurement.views import *

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateApi.as_view()),
    path('measurements/', MeasurementListView.as_view()),
    path('measurements/<int:pk>/', MeasurementListView.as_view()),
]
