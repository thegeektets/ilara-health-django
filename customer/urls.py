from django.urls import path, include
from .views import CustomerViewSet

customer_list = CustomerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
customer_detail = CustomerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:pk>/', customer_detail, name='customer-detail'),
]
