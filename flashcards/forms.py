from django import forms
from django.forms import ModelForm
from .models import Deck, Flashcard


class FlashcardForm(ModelForm):

    class Meta:
        model = Flashcard
        fields = ['question', 'answer']


class DeckForm(ModelForm):

    class Meta:
        model = Deck
        fields = ['title']
