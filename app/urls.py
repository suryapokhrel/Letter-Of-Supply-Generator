from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.generate_letter_of_supply, name='generate_letter_of_supply'),
]
