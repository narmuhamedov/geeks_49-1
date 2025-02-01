from django.urls import path
from . import views

urlpatterns = [
    path('emodji/', views.emodji, name='emodji'),
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),
]