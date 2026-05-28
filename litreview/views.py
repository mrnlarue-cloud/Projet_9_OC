from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from litreview.forms import InscriptionForm, ReviewForm, TicketForm
from litreview.models import Review, Ticket

# ----------------------------
# Accueil / flux
# ----------------------------


@login_required
def accueil(request):
    """Affichage des contenus visibles par l'utilisateur."""
    contenus_flux = request.user.contenus_flux_visible()

    return render(
        request,
        "pages/accueil.html",
        {
            "tickets_utilisateur": contenus_flux["tickets"],
            "critiques_utilisateur": contenus_flux["critiques"],
            "publications": contenus_flux["publications"],
            "tickets_deja_critiques": contenus_flux["tickets_deja_critiques"],
        },
    )


# ----------------------------
# Abonnements
# ----------------------------


@login_required
def abonnements(request):
    """Affiche les utilisateurs suivis par l'utilisateur."""
    utilisateurs_suivis = request.user.utilisateurs_suivis()

    return render(
        request,
        "pages/abonnements.html",
        {"utilisateurs_suivis": utilisateurs_suivis},
    )


# ----------------------------
# Tickets
# ----------------------------


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


# ----------------------------
# Critiques
# ----------------------------


@login_required
def creer_critique(request, ticket_id):
    """Crée une critique en réponse à un ticket."""
    ticket = get_object_or_404(Ticket.ticket_par_id(ticket_id))

    if Review.critique_deja_creee(request.user, ticket):
        return redirect("accueil")

    if request.method == "POST":
        formulaire_critique = ReviewForm(request.POST)

        if formulaire_critique.is_valid():
            donnees = formulaire_critique.cleaned_data

            Review.creer_critique_en_reponse(
                utilisateur=request.user,
                ticket=ticket,
                titre=donnees["headline"],
                commentaire=donnees["body"],
                note=donnees["rating"],
            )

            return redirect("accueil")

    else:
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
