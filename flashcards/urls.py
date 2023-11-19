from django.urls import path
from . import views

urlpatterns = [
    path('', views.deck_list, name='home'),
    path('flashcards/', views.cards, name='flashcards'),
]
