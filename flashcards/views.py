from django.shortcuts import render
from .models import Deck


# Create your views here.
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'decks': decks})
