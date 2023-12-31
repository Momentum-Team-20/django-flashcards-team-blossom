# Generated by Django 4.2.7 on 2023-11-20 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_deck_flashcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deck',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
