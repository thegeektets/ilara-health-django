from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, OrderItemViewSet, OrderStatusViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'order_statuses', OrderStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
