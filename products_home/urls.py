from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('bathroom/', views.bathroom_products, name='bathroom_products'),
    path('kitchen/', views.kitchen_products, name='kitchen_products'),
]
