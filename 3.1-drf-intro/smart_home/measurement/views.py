
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from .serializers import *


# Создаём и читаем информацию по всем датчикам
class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Изменяем информацию о конкретном датчике
class SensorUpdateApi(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializerDetail


# Добавляем данные температуры к датчику и читаем информацию по конкретному датчике и данным о температуре
class MeasurementListView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
