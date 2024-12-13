from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers, name='list_customers'),  # Main customer list view
    path('customers/add/', views.add_customer, name='add_customer'),  # Add customer view
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),  # Edit customer view
    path('customers/', views.CustomerList.as_view(), name='api_customers'),  # API for listing customers
]
