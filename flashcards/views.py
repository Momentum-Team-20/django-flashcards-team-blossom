from django.shortcuts import render, redirect
from .models import Deck, Flashcard
from .forms import DeckForm


# Create your views here.
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'decks': decks})


def cards(request, deck_number):
    flashcards = Flashcard.objects.filter(deck_id=deck_number)
    return render(request, 'flashcards/cards.html', {'flashcards': flashcards})


def create_new_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeckForm()
    return render(request, 'flashcards/create_deck.html', {'form': form})
