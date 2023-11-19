from django.shortcuts import render
from .models import Deck, Flashcard


# Create your views here.
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'decks': decks})


def cards(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/cards.html', {'flashcards': flashcards})
