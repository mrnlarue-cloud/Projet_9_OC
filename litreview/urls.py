from django.urls import path

from litreview import views

urlpatterns = [
    # ----------------------------
    # Page utilisateur
    # ----------------------------
    path("accueil/", views.accueil, name="accueil"),
    # ----------------------------
    # Abonnements
    # ----------------------------
    path("abonnements/", views.abonnements, name="abonnements"),
    # ----------------------------
    # Authentification
    # ----------------------------
    path("connexion/", views.connexion, name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("inscription/", views.inscription, name="inscription"),
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
