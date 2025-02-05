from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list_view, name='film_list'),
    path('film_detail/<int:id>/', views.film_detail_view, name='film_detail'),


    path('emodji/', views.emodji, name='emodji'),
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),
]