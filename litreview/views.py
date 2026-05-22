from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from litreview.forms import InscriptionForm

# ----------------------------
# Page test utilisateur
# ----------------------------


@login_required
def accueil(request):
    """Vue Django accessible uniquement après connexion."""
    return render(request, "pages/accueil.html")


# ----------------------------
# Inscription
# ----------------------------


def inscription(request):
    """Inscrit un nouvel utilisateur."""
    if request.method == "POST":
        formulaire_inscription = InscriptionForm(request.POST)

        if formulaire_inscription.is_valid():
            utilisateur = formulaire_inscription.save()
            login(request, utilisateur)
            return redirect("accueil")

    else:
        formulaire_inscription = InscriptionForm()

    return render(
        request,
        "pages/inscription.html",
        {"formulaire_inscription": formulaire_inscription},
    )


# ----------------------------
# Connexion
# ----------------------------


def connexion(request):
    """Connecte l'utilisateur si les identifiants sont valides."""
    if request.method == "POST":
        formulaire_connexion = AuthenticationForm(request, data=request.POST)

        if formulaire_connexion.is_valid():
            utilisateur = formulaire_connexion.get_user()
            login(request, utilisateur)
            return redirect("accueil")

    else:
        formulaire_connexion = AuthenticationForm()

    return render(
        request,
        "pages/connexion.html",
        {"formulaire_connexion": formulaire_connexion},
    )


# ----------------------------
# Déconnexion
# ----------------------------


@login_required
def deconnexion(request):
    """Déconnecte l'utilisateur."""
    logout(request)
    return redirect("connexion")
