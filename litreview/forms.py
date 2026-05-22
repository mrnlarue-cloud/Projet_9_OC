from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class Inscription(UserCreationForm):
    """Formulaire d'inscription"""

    class Meta:
        model = get_user_model()
        fields = ["username"]
