"""Modèle métier pur pour une demande de critique.

Ce fichier représente une demande créée par un utilisateur pour obtenir
une critique sur un livre ou un article.

La classe gère :
- le titre de la demande ;
- l'auteur de la demande ;
- une description optionnelle ;
- une image optionnelle ;
- les droits de modification et de suppression ;
- la vérification qu'un utilisateur peut publier une critique sur cette demande.
"""


class DemandeCritique:
    """Demande de critique créée par un utilisateur."""

    # ----------------------------
    # Initialisation
    # ----------------------------

    def __init__(self, titre, auteur, description="", image=None):
        self.titre = titre
        self.auteur = auteur
        self.description = description
        self.image = image

    # ----------------------------
    # Validation
    # ----------------------------

    def titre_valide(self):
        return isinstance(self.titre, str) and self.titre.strip() != ""

    def auteur_valide(self):
        return self.auteur is not None

    def est_valide(self):
        return self.titre_valide() and self.auteur_valide()

    # ----------------------------
    # Droits
    # ----------------------------

    def modifiable_par(self, utilisateur):
        return utilisateur is not None and utilisateur.est_auteur(self)

    def supprimable_par(self, utilisateur):
        return utilisateur is not None and utilisateur.est_auteur(self)

    # ----------------------------
    # Modification
    # ----------------------------

    def modifier(self, utilisateur, titre=None, description=None, image=None):
        if not self.modifiable_par(utilisateur):
            return False

        nouveau_titre = self.titre if titre is None else titre

        if not isinstance(nouveau_titre, str) or nouveau_titre.strip() == "":
            return False

        self.titre = nouveau_titre

        if description is not None:
            self.description = description

        if image is not None:
            self.image = image

        return True

    # ----------------------------
    # Critiques associées
    # ----------------------------

    def critique_existante(self, utilisateur, critiques_existantes):
        if utilisateur is None:
            return False

        for critique in critiques_existantes:
            meme_auteur = utilisateur.bon_utilisateur(critique.auteur)
            meme_demande = critique.demande_critique == self

            if meme_auteur and meme_demande:
                return True

        return False

    def critiquable_par(self, utilisateur, critiques_existantes):
        if utilisateur is None:
            return False

        if self.est_valide():
            if self.critique_existante(utilisateur, critiques_existantes):
                return False
            else:
                return True

        return False
