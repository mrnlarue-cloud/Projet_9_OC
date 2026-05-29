from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from litreview.forms import (
    AbonnementForm,
    InscriptionForm,
    ReviewForm,
    TicketForm,
)
from litreview.models import Review, Ticket, UserFollows

# ----------------------------
# Authentification
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


@login_required
def deconnexion(request):
    """Déconnecte l'utilisateur."""
    logout(request)
    return redirect("connexion")


# ----------------------------
# Accueil / publications
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


@login_required
def mes_posts(request):
    """Affiche les tickets et critiques créés par l'utilisateur."""
    return render(
        request,
        "pages/mes_posts.html",
        {"publications": request.user.publications_utilisateur()},
    )


# ----------------------------
# Abonnements / Désabonnements
# ----------------------------


@login_required
def abonnements(request):
    """Affiche les utilisateurs suivis et permet d'en suivre un nouveau."""
    formulaire_abonnement = AbonnementForm(request.POST or None)

    if request.method == "POST":
        abonnement_ajoute = UserFollows.traiter_formulaire_abonnement(
            utilisateur=request.user,
            formulaire_abonnement=formulaire_abonnement,
        )

        if abonnement_ajoute:
            return redirect("abonnements")

    return render(
        request,
        "pages/abonnements.html",
        {
            "utilisateurs_suivis": request.user.utilisateurs_suivis(),
            "formulaire_abonnement": formulaire_abonnement,
        },
    )


@login_required
@require_POST
def desabonnement(request, utilisateur_suivi_id):
    """Désabonnement."""
    UserFollows.supprimer_abonnement(
        utilisateur=request.user,
        utilisateur_suivi_id=utilisateur_suivi_id,
    )

    return redirect("abonnements")


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


@login_required
def modifier_ticket(request, ticket_id):
    """Modifie un ticket créé par l'utilisateur."""
    ticket = get_object_or_404(
        Ticket.ticket_modifiable(
            utilisateur=request.user,
            ticket_id=ticket_id,
        )
    )

    formulaire_ticket = TicketForm(
        request.POST or None,
        request.FILES or None,
        instance=ticket,
    )

    if ticket.modifier_avec_formulaire(formulaire_ticket):
        return redirect("mes_posts")

    return render(
        request,
        "pages/modifier_ticket.html",
        {"formulaire_ticket": formulaire_ticket},
    )


@login_required
def confirmer_suppression_ticket(request, ticket_id):
    """Affiche la page de confirmation de suppression d'un ticket."""
    ticket = get_object_or_404(
        Ticket.ticket_supprimable(
            utilisateur=request.user,
            ticket_id=ticket_id,
        )
    )

    return render(
        request,
        "pages/confirmer_suppression_ticket.html",
        {"ticket": ticket},
    )

    return render(
        request,
        "pages/confirmer_suppression_ticket.html",
        {"ticket": ticket},
    )


@login_required
@require_POST
def supprimer_ticket(request, ticket_id):
    ticket = get_object_or_404(
        Ticket.ticket_supprimable(
            utilisateur=request.user,
            ticket_id=ticket_id,
        )
    )
    ticket.supprimer()

    return redirect("mes_posts")


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


@login_required
def modifier_critique(request, critique_id):
    """Modifie une critique créée par l'utilisateur."""
    critique = get_object_or_404(
        Review.critique_modifiable(
            utilisateur=request.user,
            critique_id=critique_id,
        )
    )

    formulaire_critique = ReviewForm(
        request.POST or None,
        instance=critique,
    )

    if critique.modifier_avec_formulaire(formulaire_critique):
        return redirect("mes_posts")

    return render(
        request,
        "pages/modifier_critique.html",
        {
            "formulaire_critique": formulaire_critique,
            "critique": critique,
        },
    )
