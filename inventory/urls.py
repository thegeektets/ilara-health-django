from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, SupplierViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
