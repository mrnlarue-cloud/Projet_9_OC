class Follow:
    """Relation de follow entre deux utilisateurs."""

    # ----------------------------
    # Initialisation
    # ----------------------------

    def __init__(self, utilisateur, utilisateur_suivi):
        self.utilisateur = utilisateur
        self.utilisateur_suivi = utilisateur_suivi

    # ----------------------------
    # Validation
    # ----------------------------

    def utilisateurs_valides(self):
        utilisateur_existe = self.utilisateur is not None
        utilisateur_suivi_existe = self.utilisateur_suivi is not None

        return utilisateur_existe and utilisateur_suivi_existe

    def autofollow(self):
        """Check utilisateur essaie de se follow lui-même."""
        return self.utilisateur.bon_utilisateur(
            self.utilisateur_suivi
        )

    def existe_deja(self, follows_existants):
        for follow in follows_existants:
            meme_utilisateur = self.utilisateur.bon_utilisateur(
                follow.utilisateur
            )
            meme_utilisateur_suivi = self.utilisateur_suivi.bon_utilisateur(
                follow.utilisateur_suivi
            )

            if meme_utilisateur and meme_utilisateur_suivi:
                return True

        return False

    def est_valide(self, follows_existants):
        if self.utilisateurs_valides():
            if self.autofollow():
                return False

            if self.existe_deja(follows_existants):
                return False

            return True

        else:
            return False
