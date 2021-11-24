from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal/<str:pk>/', views.animal_modif, name='animal_modif'),
    path('equipement/<str:pk>/', views.equipement_detail, name='equipement_detail'),
]