from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username


class Deck(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateField(default=timezone.now, null=True)
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='users'
    )

    def __str__(self):
        return self.title


# Flashcards uses Deck as a foreign key, because many cards can have one deck
class Flashcard(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    deck = models.ForeignKey('Deck', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question
