from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('accounts/login', views.LoginView, name='login'),
    path('', views.deck_list, name='home'),
    path('flashcards/<int:deck_number>', views.cards, name='flashcards'),
    path('flashcards/new/', views.create_new_deck, name='new_deck'),
    path('decks/<int:pk>/new_card', views.create_new_flashcard, name='create_flashcard'),
    path('flashcards/edit_flashcard/<int:pk>', views.edit_flashcard, name='edit_flashcard'),
    path('flashcards/delete_flashcard/<int:pk>', views.delete_flashcard, name='delete_flashcard')
]
