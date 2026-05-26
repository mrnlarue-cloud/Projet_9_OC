from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from litreview.models import Ticket, Review


class InscriptionForm(UserCreationForm):
    """Formulaire d'inscription pour le modèle utilisateur personnalisé."""

    class Meta:
        model = get_user_model()
        fields = ["username"]


class TicketForm(forms.ModelForm):
    """Formulaire de création d'un ticket"""

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre",
            "description": "Description",
            "image": "Image",
        }


class ReviewForm(forms.ModelForm):
    """Formulaire de création d'une critique"""

    class Meta:
        model = Review
        fields = ["headline", "body", "rating"]
        labels = {
            "headline": "Titre",
            "body": "Commentaire",
            "rating": "Notation",
        }
