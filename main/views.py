from django.core.exceptions import ValidationError
from rest_framework.response import Response

from main import models, serializers

from rest_framework import viewsets

# Create your views here.


class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

    def destroy(self, request, *args, **kwargs):
        if self.get_object().cars.all():
            return Response(
                {
                    "message": "A brand that has related car models cannot be deleted",
                    "status": 500,
                },
                500,
            )
        return super().destroy(request, *args, **kwargs)


class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
