"""Modèles Django principaux de l'application LITRevu.

Ce fichier contient les modèles reliés à la base de données :
- l'utilisateur personnalisé ;
- les demandes de critique ;
- les critiques publiées ;
- les relations de suivi entre utilisateurs.
"""

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# ----------------------------
# Utilisateur personnalisé
# ----------------------------


class User(AbstractUser):
    """Utilisateur personnalisé de l'application LITRevu."""


# ----------------------------
# Demandes de critique
# ----------------------------


class Ticket(models.Model):
    """Demande de critique créée par un utilisateur."""

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    image = models.ImageField(upload_to="tickets/", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def creer_ticket_suite_demande(
        classe_ticket,
        utilisateur,
        titre,
        description="",
        image=None,
    ):
        """Crée un ticket associé à un utilisateur"""
        return classe_ticket.objects.create(
            user=utilisateur,
            title=titre,
            description=description,
            image=image,
        )

    @classmethod
    def tickets_utilisateur(classe_ticket, utilisateur):
        """Retourne les tickets d'un utilisateur du plus récent au plus ancien"""
        return classe_ticket.objects.filter(user=utilisateur).order_by("-time_created")

    def __str__(self):
        """Retourne le titre du ticket."""
        return self.title


# ----------------------------
# Critiques publiées
# ----------------------------


class Review(models.Model):
    """Critique publiée par un utilisateur."""

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    headline = models.CharField(max_length=128, blank=False)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Contraintes."""

        unique_together = ("ticket", "user")

    def __str__(self):
        """Retourne le titre de la critique."""
        return self.headline


# ----------------------------
# Relations de suivi
# ----------------------------


class UserFollows(models.Model):
    """Relation de suivi entre deux utilisateurs."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        """Contraintes."""

        unique_together = ("user", "followed_user")

    def __str__(self):
        """Retourne une phrase décrivant la relation de suivi."""
        return f"{self.user} suit {self.followed_user}"
