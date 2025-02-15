from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name='film_list'),
    path('film_detail/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('create_review/', views.create_review_view, name='create_review'),

    path('emodji/', views.emodji, name='emodji'),
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),
    path('search/', views.SearchView.as_view(), name='search'),
]