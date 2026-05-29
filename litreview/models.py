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

    def utilisateurs_visibles(self):
        """Retourne l'utilisateur et les utilisateurs suivis."""
        abonnements = UserFollows.objects.filter(user=self)

        utilisateurs_visibles = {self}

        for abonnement in abonnements:
            utilisateurs_visibles.add(abonnement.followed_user)

        return utilisateurs_visibles

    def utilisateurs_suivis(self):
        """Retourne les utilisateurs suivis par l'utilsateur"""
        abonnements = UserFollows.objects.filter(user=self).select_related(
            "followed_user"
        )

        utilisateurs = []

        for abonnement in abonnements:
            utilisateurs.append(abonnement.followed_user)

        return utilisateurs

    def tickets_deja_critiques(self):
        """Retourne les IDs des tickets déjà critiqués."""
        critiques_utilisateur = Review.objects.filter(user=self)

        ids_tickets = set()

        for critique in critiques_utilisateur:
            ids_tickets.add(critique.ticket.id)

        return ids_tickets

    def contenus_flux_visible(self):
        """Retourne les contenus visibles dans le flux."""
        tickets_visibles = Ticket.tickets_visibles_utilisateur(self)
        critiques_visibles = Review.critiques_visibles_utilisateur(self)
        publications = self.publications_flux(
            tickets_visibles=tickets_visibles,
            critiques_visibles=critiques_visibles,
        )

        return {
            "tickets": tickets_visibles,
            "critiques": critiques_visibles,
            "publications": publications,
            "tickets_deja_critiques": self.tickets_deja_critiques(),
        }

    def publications_utilisateur(self):
        """Retourne les tickets et critiques créés par l'utilisateur."""
        tickets_utilisateur = Ticket.tickets_utilisateur(self)
        critiques_utilisateur = Review.critiques_utilisateur(self)

        return self.publications_flux(
            tickets_visibles=tickets_utilisateur,
            critiques_visibles=critiques_utilisateur,
        )

    def publications_flux(self, tickets_visibles, critiques_visibles):
        """Retourne tickets et critiques dans une seule liste triée."""
        publications = []

        for ticket in tickets_visibles:
            publications.append(
                {
                    "categorie": "ticket",
                    "objet": ticket,
                    "date": ticket.time_created,
                }
            )

        for critique in critiques_visibles:
            publications.append(
                {
                    "categorie": "critique",
                    "objet": critique,
                    "date": critique.time_created,
                }
            )

        publications.sort(
            key=lambda publication: publication["date"],
            reverse=True,
        )

        return publications


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
    image = models.ImageField(upload_to="tickets_images/", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def creer_ticket_suite_demande(
        classe_ticket,
        utilisateur,
        titre,
        description="",
        image=None,
    ):
        """Crée un ticket associé à un utilisateur."""
        return classe_ticket.objects.create(
            user=utilisateur,
            title=titre,
            description=description,
            image=image,
        )

    @classmethod
    def tickets_utilisateur(classe_ticket, utilisateur):
        """Retourne les tickets d'un utilisateur du plus récent au plus ancien."""
        return classe_ticket.objects.filter(user=utilisateur).order_by("-time_created")

    @classmethod
    def tickets_visibles_utilisateur(classe_ticket, utilisateur):
        """Retourne les tickets visibles dans le flux."""
        utilisateurs_visibles = utilisateur.utilisateurs_visibles()

        return classe_ticket.objects.filter(user__in=utilisateurs_visibles).order_by(
            "-time_created"
        )

    @classmethod
    def ticket_par_id(classe_ticket, ticket_id):
        """Retourne une requête filtrée sur l'ID."""
        return classe_ticket.objects.filter(id=ticket_id)

    @classmethod
    def ticket_modifiable(classe_ticket, utilisateur, ticket_id):
        """Retourne le ticket modifiable par l'utilisateur."""
        return classe_ticket.objects.filter(
            id=ticket_id,
            user=utilisateur,
        )

    def modifier_avec_formulaire(self, formulaire_ticket):
        """Modifie le ticket si le formulaire est valide."""
        if not formulaire_ticket.is_bound:
            return False

        if not formulaire_ticket.is_valid():
            return False

        formulaire_ticket.save()
        return True

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

    @classmethod
    def creer_critique_en_reponse(
        classe_review,
        utilisateur,
        ticket,
        titre,
        commentaire="",
        note=0,
    ):
        """Crée une critique en réponse à un ticket."""
        return classe_review.objects.create(
            user=utilisateur,
            ticket=ticket,
            headline=titre,
            body=commentaire,
            rating=note,
        )

    @classmethod
    def critique_deja_creee(classe_review, utilisateur, ticket):
        """Check si une critique a déjà été faite par l'utilisateur."""
        return classe_review.objects.filter(
            user=utilisateur,
            ticket=ticket,
        ).exists()

    @classmethod
    def critique_modifiable(classe_review, utilisateur, critique_id):
        """Retourne la critique modifiable par l'utilisateur."""
        return classe_review.objects.filter(
            id=critique_id,
            user=utilisateur,
        )

    def modifier_avec_formulaire(self, formulaire_critique):
        """Modifie la critique si le formulaire est valide."""
        if not formulaire_critique.is_bound:
            return False

        if not formulaire_critique.is_valid():
            return False

        formulaire_critique.save()
        return True

    @classmethod
    def critiques_utilisateur(classe_review, utilisateur):
        """Retourne les critiques d'un utilisateur."""
        return classe_review.objects.filter(user=utilisateur).order_by("-time_created")

    @classmethod
    def critiques_visibles_utilisateur(classe_review, utilisateur):
        """Retourne les critiques visibles dans le flux."""
        utilisateurs_visibles = utilisateur.utilisateurs_visibles()

        critiques_utilisateurs_visibles = classe_review.objects.filter(
            user__in=utilisateurs_visibles
        )

        tickets_utilisateur = Ticket.tickets_utilisateur(utilisateur)

        critiques_sur_mes_tickets = classe_review.objects.filter(
            ticket__in=tickets_utilisateur
        )

        ids_critiques_visibles = set()

        for critique in critiques_utilisateurs_visibles:
            ids_critiques_visibles.add(critique.id)

        for critique in critiques_sur_mes_tickets:
            ids_critiques_visibles.add(critique.id)

        return classe_review.objects.filter(id__in=ids_critiques_visibles).order_by(
            "-time_created"
        )

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

    @classmethod
    def ajout_abonnement(classe_abonnement, utilisateur, username):
        """Ajoute un abonnement à partir d'un nom d'utilisateur."""
        try:
            utilisateur_a_suivre = User.objects.get(username=username)
        except User.DoesNotExist:
            return "Cet utilisateur n'existe pas."

        if utilisateur_a_suivre == utilisateur:
            return "Vous ne pouvez pas vous suivre vous-même."

        abonnement_existe = classe_abonnement.objects.filter(
            user=utilisateur,
            followed_user=utilisateur_a_suivre,
        ).exists()

        if abonnement_existe:
            return "Vous suivez déjà cet utilisateur."

        classe_abonnement.objects.create(
            user=utilisateur,
            followed_user=utilisateur_a_suivre,
        )

        return None

    @classmethod
    def traiter_formulaire_abonnement(
        classe_abonnement,
        utilisateur,
        formulaire_abonnement,
    ):
        """Traite le formulaire d'abonnement."""
        if not formulaire_abonnement.is_valid():
            return False

        username = formulaire_abonnement.cleaned_data["username"]

        erreur = classe_abonnement.ajout_abonnement(
            utilisateur=utilisateur,
            username=username,
        )

        if erreur:
            formulaire_abonnement.add_error("username", erreur)
            return False

        return True

    @classmethod
    def supprimer_abonnement(
        classe_abonnement,
        utilisateur,
        utilisateur_suivi_id,
    ):
        """Supprime un follow."""
        abonnement = classe_abonnement.objects.filter(
            user=utilisateur,
            followed_user_id=utilisateur_suivi_id,
        ).first()

        if abonnement:
            abonnement.delete()

    def __str__(self):
        """Retourne une phrase décrivant la relation de suivi."""
        return f"{self.user} suit {self.followed_user}"
