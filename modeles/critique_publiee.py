class CritiquePubliee:
    """Critique publiée par un utilisateur"""

    note_maximale = 5
    note_minimale = 0

    # ----------------------------
    # Initialisation
    # ----------------------------

    def __init__(self, titre, commentaire, note, auteur, demande_critique):
        self.titre = titre
        self.commentaire = commentaire
        self.note = note
        self.auteur = auteur
        self.demande_critique = demande_critique

    # ----------------------------
    # Validation
    # ----------------------------

    def titre_valide(self):
        return isinstance(self.titre, str) and self.titre.strip() != ""

    def note_valide(self):
        return (
            isinstance(self.note, int)
            and self.note_minimale <= self.note <= self.note_maximale
        )

    def auteur_valide(self):
        return self.auteur is not None

    def demande_valide(self):
        return self.demande_critique is not None

    def est_valide(self):
        return (
            self.titre_valide()
            and self.note_valide()
            and self.auteur_valide()
            and self.demande_valide()
        )

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

    def modifier(self, utilisateur, titre=None, commentaire=None, note=None):
        if self.modifiable_par(utilisateur):
            nouveau_titre = self.titre
            nouveau_commentaire = self.commentaire
            nouvelle_note = self.note

            if titre is not None:
                nouveau_titre = titre

            if commentaire is not None:
                nouveau_commentaire = commentaire

            if note is not None:
                nouvelle_note = note

            titre_invalide = (
                not isinstance(nouveau_titre, str) or nouveau_titre.strip() == ""
            )

            note_invalide = (
                not isinstance(nouvelle_note, int)
                or nouvelle_note < self.note_minimale
                or nouvelle_note > self.note_maximale
            )

            if titre_invalide:
                return False

            if note_invalide:
                return False

            self.titre = nouveau_titre
            self.commentaire = nouveau_commentaire
            self.note = nouvelle_note

            return True

        else:
            return False
