from django.urls import path

from apps.post.views import CarAPIView

urlpatterns = [
    path('', CarAPIView.as_view(), name='api_car')
]