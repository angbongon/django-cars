from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField("Name", max_length=250, unique=True)
    creation_date = models.DateTimeField("Creation date", null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)


class Car(models.Model):
    name = models.CharField("Name", max_length=250)
    height = models.DecimalField("Height", max_digits=10, decimal_places=2)
    width = models.DecimalField("Width", max_digits=10, decimal_places=2)

    brand = models.ForeignKey(Brand, related_name="cars", on_delete=models.PROTECT)
