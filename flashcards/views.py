from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm


@login_required
def deck_list(request):
    decks = Deck.objects.filter(user=request.user)
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


def create_new_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/create_flashcard.html', {'form': form})


def edit_flashcard(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    decks = Deck.objects.filter

    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('flashcards', deck_number=flashcard.deck.pk)
            # return render(request, 'flashcards/cards.html', { 'deck': flashcard.deck.title})
    else:
        form = FlashcardForm(instance=flashcard)
    return render(request, 'flashcards/index.html', {'decks': decks})
# <django.db.models.query_utils.DeferredAttribute object at 0x1028eb110>


def delete_flashcard(request, pk):
    form = get_object_or_404(Flashcard, pk=pk)
    form.delete()
    return redirect('home')
