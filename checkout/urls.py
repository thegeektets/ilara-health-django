from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:checkout_id>/', views.checkout_detail, name='checkout_detail'),
    path('checkout/<int:checkout_id>/add_order/', views.add_order, name='add_order'),
    path('checkout/<int:checkout_id>/remove_order/<int:order_id>/', views.remove_order, name='remove_order'),
    path('checkout/<int:checkout_id>/complete/', views.complete_checkout, name='complete_checkout'),
]
