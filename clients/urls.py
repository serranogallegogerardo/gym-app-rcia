from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Ruta principal: Dashboard
    path('client/<int:pk>/', views.client_detail, name='client_detail'),  # Detalles de un cliente
    path('payments/', views.payments, name='payments'),  # Listado de pagos pendientes
]