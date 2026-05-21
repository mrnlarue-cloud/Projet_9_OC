from django.urls import path

from litreview import views

urlpatterns = [
    path("accueil/", views.accueil, name="accueil"),
]