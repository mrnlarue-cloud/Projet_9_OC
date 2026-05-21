from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


@login_required
def accueil(request):
    """Vue django pour obligation de connexion"""
    return render(request, "pages/accueil.html")


def connexion(request):
    """Affiche le formulaire de connexion."""
    formulaire_connexion = AuthenticationForm()
    return render(
        request,
        "pages/connexion.html",
        {"formulaire_connexion": formulaire_connexion},
    )
