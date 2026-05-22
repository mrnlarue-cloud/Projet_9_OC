from django.urls import path

from litreview import views

urlpatterns = [
    path("accueil/", views.accueil, name="accueil"),
    path("connexion/", views.connexion, name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("inscription/", views.inscription, name="inscription"),
]