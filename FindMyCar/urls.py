from django.urls import path
from . import views

urlpatterns = [
    path('', views.finder_home, name='finder_home'),
    path('findCars', views.display_cars, name='display_cars'),
]
