from rest_framework import routers
from .views import CheckoutViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'checkout', CheckoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]