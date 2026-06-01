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
from litreview.models import Review, Ticket, User, UserFollows

# ----------------------------
# Authentification
# ----------------------------


def inscription(request):
    """Inscrit un nouvel utilisateur."""
    formulaire_inscription = InscriptionForm(request.POST or None)

    utilisateur = User.creer_depuis_formulaire(formulaire_inscription)

    if utilisateur:
        login(request, utilisateur)
        return redirect("accueil")

    return render(
        request,
        "pages/inscription.html",
        {"formulaire_inscription": formulaire_inscription},
    )


def connexion(request):
    """Connecte l'utilisateur si les identifiants sont valides."""
    formulaire_connexion = AuthenticationForm(
        request,
        data=request.POST or None,
    )

    if formulaire_connexion.is_valid():
        utilisateur = formulaire_connexion.get_user()
        login(request, utilisateur)
        return redirect("accueil")

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
    """Affiche les contenus visibles par l'utilisateur."""
    return render(
        request,
        "pages/accueil.html",
        request.user.contexte_accueil(),
    )


@login_required
def mes_posts(request):
    """Affiche les tickets et critiques créés par l'utilisateur."""
    return render(
        request,
        "pages/mes_posts.html",
        request.user.contexte_mes_posts(),
    )


# ----------------------------
# Abonnements / Désabonnements
# ----------------------------


@login_required
def abonnements(request):
    """Affiche les utilisateurs suivis et permet d'en suivre un nouveau."""
    formulaire_abonnement = AbonnementForm(request.POST or None)

    abonnement_ajoute = UserFollows.traiter_formulaire_abonnement(
        utilisateur=request.user,
        formulaire_abonnement=formulaire_abonnement,
    )

    if abonnement_ajoute:
        return redirect("abonnements")

    return render(
        request,
        "pages/abonnements.html",
        request.user.contexte_abonnements(formulaire_abonnement),
    )


@login_required
def confirmer_desabonnement(request, utilisateur_suivi_id):
    """Affiche la confirmation de désabonnement."""
    abonnement = get_object_or_404(
        UserFollows.abonnement_supprimable(
            utilisateur=request.user,
            utilisateur_suivi_id=utilisateur_suivi_id,
        )
    )

    return render(
        request,
        "pages/confirmer_desabonnement.html",
        {"abonnement": abonnement},
    )


@login_required
@require_POST
def desabonnement(request, utilisateur_suivi_id):
    """Désabonne l'utilisateur connecté d'un autre utilisateur."""
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
    """Crée une demande de critique."""
    formulaire_ticket = TicketForm(
        request.POST or None,
        request.FILES or None,
    )

    ticket = Ticket.creer_depuis_formulaire(
        utilisateur=request.user,
        formulaire_ticket=formulaire_ticket,
    )

    if ticket:
        return redirect("accueil")

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

    if request.method == "POST":
        formulaire_ticket = TicketForm(
            request.POST,
            request.FILES,
            instance=ticket,
        )

        if ticket.modifier_avec_formulaire(formulaire_ticket):
            return redirect("mes_posts")

    else:
        formulaire_ticket = TicketForm(instance=ticket)

    return render(
        request,
        "pages/modifier_ticket.html",
        {"formulaire_ticket": formulaire_ticket},
    )


@login_required
def confirmer_suppression_ticket(request, ticket_id):
    """Affiche la confirmation de suppression d'un ticket."""
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


@login_required
@require_POST
def supprimer_ticket(request, ticket_id):
    """Supprime un ticket créé par l'utilisateur."""
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
def creer_critique_avec_ticket(request):
    """Crée un ticket et une critique associée en une seule étape."""
    formulaire_ticket = TicketForm(
        request.POST or None,
        request.FILES or None,
    )
    formulaire_critique = ReviewForm(request.POST or None)

    creation = Review.creer_avec_ticket_depuis_formulaires(
        utilisateur=request.user,
        formulaire_ticket=formulaire_ticket,
        formulaire_critique=formulaire_critique,
    )

    if creation:
        return redirect("accueil")

    return render(
        request,
        "pages/creer_critique_avec_ticket.html",
        {
            "formulaire_ticket": formulaire_ticket,
            "formulaire_critique": formulaire_critique,
        },
    )


@login_required
def creer_critique(request, ticket_id):
    """Crée une critique en réponse à un ticket."""
    ticket = get_object_or_404(Ticket.ticket_par_id(ticket_id))

    formulaire_critique = ReviewForm(request.POST or None)

    critique = Review.creer_depuis_formulaire(
        utilisateur=request.user,
        ticket=ticket,
        formulaire_critique=formulaire_critique,
    )

    if critique:
        return redirect("accueil")

    if Review.critique_deja_creee(request.user, ticket):
        return redirect("accueil")

    return render(
        request,
        "pages/creer_critique.html",
        {
            "formulaire_critique": formulaire_critique,
            "ticket": ticket,
        },
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


@login_required
def confirmer_suppression_critique(request, critique_id):
    """Affiche la confirmation de suppression d'une critique."""
    critique = get_object_or_404(
        Review.critique_supprimable(
            utilisateur=request.user,
            critique_id=critique_id,
        )
    )

    return render(
        request,
        "pages/confirmer_suppression_critique.html",
        {"critique": critique},
    )


@login_required
@require_POST
def supprimer_critique(request, critique_id):
    """Supprime une critique créée par l'utilisateur."""
    critique = get_object_or_404(
        Review.critique_supprimable(
            utilisateur=request.user,
            critique_id=critique_id,
        )
    )

    critique.supprimer()

    return redirect("mes_posts")
