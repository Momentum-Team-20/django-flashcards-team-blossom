from django import forms
from django.forms import ModelForm
from .models import Deck, Flashcard


class FlashcardForm(ModelForm):

    class Meta:
        model = Flashcard
        fields = ['question', 'answer', 'deck']


class DeckForm(ModelForm):
    created_at = forms.DateField()

    class Meta:
        model = Deck
        fields = ['title', 'created_at']


