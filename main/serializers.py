from django.db.models.fields import DateTimeField
from main import models

from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field='name', queryset=models.Brand.objects.all())

    class Meta:
        model = models.Car
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Brand
        fields = "__all__"