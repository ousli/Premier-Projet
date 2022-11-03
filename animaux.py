from random import randint

class Animaux():
    """
    Animal pour une simulation

    Attributs :
        _gain_nourriture : entier positif, energie gagnée en mangeant
        _position : tuple, abscisse et ordonnée de l'animal
        _energie : entier positif, energie dont dispose l'animal

    Méthodes :
        __init__() : Constructeur de la classe Animaux
        deplacement() : Fais se déplacer l'animal
        get_gain_nourriture() : Renvoie combien d'énergie l'animal obtient en mangeant
        set_position() : Change la position de l'animal
        get_position() : Renvoie la position de l'animal
        set_energie() : Change l'énergie de l'animal
        get_energie() : Renvoie l'énergie de l'animal
    """

    def __init__(self, gain_nourriture, position, energie):
        """
        Constructeur de la classe Animaux
        Données:
            _gain_nourriture : entier positif, energie gagnée en mangeant
            _position : tuple, abscisse et ordonnée de l'animal
            _energie : entier, energie dont dispose l'animal
        Résultat:
            Crée un nouvel animal, ne renvoie rien
        """
        self._gain_nourriture = gain_nourriture
        self._position = position
        self._energie = energie

    def deplacement(self, monde):
        """
        Fais se déplacer l'animal
        Données:
            monde: Objet de type monde, matrice dans lequel se trouve l'animal
        Résultat:
            Déplace l'animal, ne renvoie rien
        """
        i, j = randint(-1, 1), randint(-1, 1)
        i += self.get_position()[0]
        j += self.get_position()[1]

        if i > monde.get_dimension() - 1:
            i = 0
        else:
            if i < 0:
                i = monde.get_dimension() - 1
        if j > monde.get_dimension() - 1:
            j = 0
        else:
            if j  < 0:
                j = monde.get_dimension() - 1

        self.set_position(i, j)

    def get_gain_nourriture(self):
        """
        Renvoie combien d'énergie l'animal obtient en mangeant
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier positif, énergie obtenue par l'animal en mangeant
        """
        return self._gain_nourriture

    def set_position(self, i ,j):
        """
        Change la position de l'animal
        Données:
            i : entier positif ou nul, abscisse de l'animal
            j : entier positif ou nul, ordonnée de l'animal
        Résultat : Change la position de l'animal à un abscisse et une ordonnée donnés, ne renvoie rien
        """
        self._position = (i, j)

    def get_position(self):
        """
        Renvoie la position de l'animal
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un tuple, position de l'animal
        """
        return self._position

    def set_energie(self, energie):
        """
        Change l'énergie de l'animal
        Données:
            energie: Nombre entier, énergie que l'on veut mettre à l'animal
        Résultat : Change l'énergie de l'animal, ne renvoie rien
        """
        self._energie = energie

    def get_energie(self):
        """
        Renvoie l'énergie de l'animal
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier, énergie dont dispose l'animal
        """
        return self._energie
