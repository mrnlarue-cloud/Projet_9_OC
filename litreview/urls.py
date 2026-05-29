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
    # ----------------------------
    # Abonnements
    # ----------------------------
    path("abonnements/", views.abonnements, name="abonnements"),
    path(
        "desabonnement/<int:utilisateur_suivi_id>/",
        views.desabonnement,
        name="desabonnement",
    ),
    # ----------------------------
    # Tickets
    # ----------------------------
    path("creer-ticket/", views.creer_ticket, name="creer_ticket"),
    # ----------------------------
    # Critiques
    # ----------------------------
    path(
        "creer-critique/<int:ticket_id>/",
        views.creer_critique,
        name="creer_critique",
    ),
]
