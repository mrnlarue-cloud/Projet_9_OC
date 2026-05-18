class Utilisateur:
    """Utilisateur inscrit sur LITRevu"""

    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    def bon_utilisateur(self, autre_utilisateur):
        if autre_utilisateur is None:
            return False
        return self.nom_utilisateur == autre_utilisateur.nom_utilisateur

    def est_auteur(self, contenu):
        return contenu.auteur == self

    def peut_modifier(self, contenu):
        return self.est_auteur(contenu)

    def peut_supprimer(self, contenu):
        return self.est_auteur(contenu)

    def peut_creer_demande_critique(self):
        return True

    def peut_publier_critique(self, demande_critique, critiques_existantes):
        for critique in critiques_existantes:
            meme_auteur = critique.auteur == self
            meme_demande = critique.demande_critique == demande_critique

            if meme_auteur and meme_demande:
                return False
        return True
