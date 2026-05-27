from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from litreview.forms import InscriptionForm, ReviewForm, TicketForm
from litreview.models import Ticket

# ----------------------------
# Page utilisateur
# ----------------------------


@login_required
def accueil(request):
    """Affichage des tickets de l'utilisateur"""
    tickets_utilisateur = Ticket.tickets_visibles_utilisateur(request.user)

    return render(
        request,
        "pages/accueil.html",
        {"tickets_utilisateur": tickets_utilisateur},
    )


@login_required
def creer_ticket(request):
    """Crée une demande d'avis utilisateur."""
    if request.method == "POST":
        formulaire_ticket = TicketForm(request.POST, request.FILES)

        if formulaire_ticket.is_valid():
            donnees = formulaire_ticket.cleaned_data

            Ticket.creer_ticket_suite_demande(
                utilisateur=request.user,
                titre=donnees["title"],
                description=donnees["description"],
                image=donnees["image"],
            )

            return redirect("accueil")

    else:
        formulaire_ticket = TicketForm()

    return render(
        request,
        "pages/creer_ticket.html",
        {"formulaire_ticket": formulaire_ticket},
    )


@login_required
def creer_critique(request, ticket_id):
    """Prépare la création d'une critique en réponse à un ticket"""
    ticket = get_object_or_404(Ticket.ticket_par_id(ticket_id))
    formulaire_critique = ReviewForm()

    return render(
        request,
        "pages/creer_critique.html",
        {"formulaire_critique": formulaire_critique, "ticket": ticket},
    )


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
