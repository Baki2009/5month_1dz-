from rest_framework.generics import ListAPIView, CreateAPIView

from apps.post.models import Car
from apps.post.serializers import CarSerializer

# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer