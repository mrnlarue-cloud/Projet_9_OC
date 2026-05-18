class Follow:
    """Relation de follow entre deux utilisateurs."""

    def __init__(self, utilisateur, utilisateur_suivi):
        self.utilisateur = utilisateur
        self.utilisateur_suivi = utilisateur_suivi

    def autofollow(self):
        """Vérifie si un utilisateur essaie de se follow lui-même."""
        return self.utilisateur.bon_utilisateur(self.utilisateur_suivi)

    def existe_deja(self, follows_existants):
        for follow in follows_existants:
            meme_utilisateur = self.utilisateur.bon_utilisateur(follow.utilisateur)
            meme_utilisateur_suivi = self.utilisateur_suivi.bon_utilisateur(
                follow.utilisateur_suivi
            )

            if meme_utilisateur and meme_utilisateur_suivi:
                return True

        return False

    def est_valide(self, follows_existants):
        if self.autofollow():
            return False

        if self.existe_deja(follows_existants):
            return False

        return True
