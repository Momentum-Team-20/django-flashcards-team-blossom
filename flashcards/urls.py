from django.urls import path
from . import views

urlpatterns = [
    path('', views.deck_list, name='home'),
    path('flashcards/<int:pk>', views.cards, name='flashcards'),
]
