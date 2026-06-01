from django.urls import path
from django.views.generic import RedirectView

from litreview import views

urlpatterns = [
    # ----------------------------
    # Racine du site
    # ----------------------------
    path(
        "",
        RedirectView.as_view(pattern_name="accueil", permanent=False),
        name="racine",
    ),
    # ----------------------------
    # Authentification
    # ----------------------------
    path("connexion/", views.connexion, name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("inscription/", views.inscription, name="inscription"),
    # ----------------------------
    # Page utilisateur
    # ----------------------------
    path("accueil/", views.accueil, name="accueil"),
    path("mes-posts/", views.mes_posts, name="mes_posts"),
    # ----------------------------
    # Abonnements
    # ----------------------------
    path("abonnements/", views.abonnements, name="abonnements"),
    path(
        "desabonnement/<int:utilisateur_suivi_id>/",
        views.confirmer_desabonnement,
        name="confirmer_desabonnement",
    ),
    path(
        "desabonnement/<int:utilisateur_suivi_id>/confirmer/",
        views.desabonnement,
        name="desabonnement",
    ),
    # ----------------------------
    # Tickets
    # ----------------------------
    path("creer-ticket/", views.creer_ticket, name="creer_ticket"),
    path(
        "modifier-ticket/<int:ticket_id>/",
        views.modifier_ticket,
        name="modifier_ticket",
    ),
    path(
        "supprimer-ticket/<int:ticket_id>/",
        views.confirmer_suppression_ticket,
        name="confirmer_suppression_ticket",
    ),
    path(
        "supprimer-ticket/<int:ticket_id>/confirmer/",
        views.supprimer_ticket,
        name="supprimer_ticket",
    ),
    # ----------------------------
    # Critiques
    # ----------------------------
    path(
        "creer-critique/",
        views.creer_critique_avec_ticket,
        name="creer_critique_avec_ticket",
    ),
    path(
        "creer-critique/<int:ticket_id>/",
        views.creer_critique,
        name="creer_critique",
    ),
    path(
        "modifier-critique/<int:critique_id>/",
        views.modifier_critique,
        name="modifier_critique",
    ),
    path(
        "supprimer-critique/<int:critique_id>/",
        views.confirmer_suppression_critique,
        name="confirmer_suppression_critique",
    ),
    path(
        "supprimer-critique/<int:critique_id>/confirmer/",
        views.supprimer_critique,
        name="supprimer_critique",
    ),
]
