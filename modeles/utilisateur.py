class Utilisateur:
    """Utilisateur inscrit sur LITRevu."""

    # ----------------------------
    # Initialisation
    # ----------------------------

    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    # ----------------------------
    # Identification utilisateur
    # ----------------------------

    def nom_valide(self):
        return (
            isinstance(self.nom_utilisateur, str) and self.nom_utilisateur.strip() != ""
        )

    def bon_utilisateur(self, autre_utilisateur):
        if autre_utilisateur is None:
            return False

        return self.nom_utilisateur == autre_utilisateur.nom_utilisateur

    # ----------------------------
    # Droits sur les contenus
    # ----------------------------

    def est_auteur(self, contenu):
        if contenu is None:
            return False

        return self.bon_utilisateur(contenu.auteur)

    def peut_modifier(self, contenu):
        return self.est_auteur(contenu)

    def peut_supprimer(self, contenu):
        return self.est_auteur(contenu)

    # ----------------------------
    # Demandes de critique
    # ----------------------------

    def peut_creer_demande_critique(self):
        return self.nom_valide()

    # ----------------------------
    # Critiques publiées
    # ----------------------------

    def a_deja_publie_critique(self, demande_critique, critiques_existantes):
        for critique in critiques_existantes:
            meme_auteur = self.bon_utilisateur(critique.auteur)
            meme_demande = critique.demande_critique == demande_critique

            if meme_auteur and meme_demande:
                return True

        return False

    def peut_publier_critique(self, demande_critique, critiques_existantes):
        if demande_critique is None:
            return False

        if not self.nom_valide():
            return False

        return not self.a_deja_publie_critique(
            demande_critique,
            critiques_existantes,
        )

    # ----------------------------
    # Follows
    # ----------------------------

    def suit_deja(self, utilisateur_suivi, follows_existants):
        if utilisateur_suivi is None:
            return False

        for follow in follows_existants:
            meme_utilisateur = self.bon_utilisateur(follow.utilisateur)
            meme_utilisateur_suivi = utilisateur_suivi.bon_utilisateur(
                follow.utilisateur_suivi
            )

            if meme_utilisateur and meme_utilisateur_suivi:
                return True

        return False

    def peut_follow(self, utilisateur_suivi, follows_existants):
        if utilisateur_suivi is None:
            return False

        if not self.nom_valide():
            return False

        if self.bon_utilisateur(utilisateur_suivi):
            return False

        return not self.suit_deja(utilisateur_suivi, follows_existants)
