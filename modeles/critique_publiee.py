class CritiquePubliee:
    """Critique publiée par un utilisateur"""

    note_maximale = 5
    note_minimale = 0

    def __init__(self, titre, commentaire, note, auteur, demande_critique):
        self.titre = titre
        self.commentaire = commentaire
        self.note = note
        self.auteur = auteur
        self.demande_critique = demande_critique

    def note_valide(self):
        return self.note_minimale <= self.note <= self.note_maximale

    def modifiable_par(self, utilisateur):
        return utilisateur.est_auteur(self)

    def supprimable_par(self, utilisateur):
        return utilisateur.est_auteur(self)
