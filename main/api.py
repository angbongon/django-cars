from django.urls import path, include

from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register(r"carbrands", views.BrandViewSet)
router.register(r"carmodels", views.CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
