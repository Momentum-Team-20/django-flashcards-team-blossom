from django.urls import path
from . import views

urlpatterns = [
    path('', views.deck_list, name='home'),
    path('flashcards/<int:deck_number>', views.cards, name='flashcards'),
    path('flashcards/new/', views.create_new_deck, name='new_deck'),
]
