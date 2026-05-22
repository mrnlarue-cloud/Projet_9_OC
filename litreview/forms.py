from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class InscriptionForm(UserCreationForm):
    """Formulaire d'inscription pour le modèle utilisateur personnalisé."""

    class Meta:
        model = get_user_model()
        fields = ["username"]
