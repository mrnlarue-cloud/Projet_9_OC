class DemandeCritique:
    """Demande de critique créée par un utilisateur"""

    def __init__(self, titre, auteur, description="", image=None):
        self.titre = titre
        self.auteur = auteur
        self.description = description
        self.image = image

    def modifiable_par(self, utilisateur):
        return utilisateur.est_auteur(self)

    def supprimable_par(self, utilisateur):
        return utilisateur.est_auteur(self)

    def critique_existante(self, utilisateur, critiques_existantes):
        for critique in critiques_existantes:
            meme_auteur = critique.auteur == utilisateur
            meme_demande = critique.demande_critique == self

            if meme_auteur and meme_demande:
                return True

        return False
