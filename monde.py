from random import randint

class Monde():
    """
    Monde pour une simulation

    Attributs:
        _duree_repousse : Entier positif, Coefficient à partire duquel l'herbe aura poussée
        _dimension : Entier positif supérieur ou égal à 50, taille de la matrice
        _carte : Liste, matrice contenant tout les coefficients de pousse de l'herbe

    Méthodes:
        __init__() : Constructeur de la classe Monde
        herbe_pousse() : Fais pousser l'herbe de la carte
        herbe_mangee() : Renvoie le status de l'herbe à une position donnée
        nb_herbe() : Renvoie le nombre de carré d'herbe poussés
        get_coef_carte() : Renvoi un coefficient de la matrice
        set_coef_carte() : Change un coefficient de la matrice
        get_dimension() : Renvoi les dimension de la carte
        get_carte() : Renvoi la carte
    """
    def __init__(self, dimension, duree_repousse):
        """
        Constructeur de la classe Monde
        Données:
            _duree_repousse : Entier positif, Coefficient à partire duquel l'herbe aura poussée
            _dimension : Entier positif supérieur ou égal à 50, taille de la matrice
            _carte : Liste, matrice contenant tout les coefficients de pousse de l'herbe
        Résultat
            Crée un nouveau monde, ne renvoie rien
        """
        self._duree_repousse = duree_repousse
        if dimension < 50:
            self._dimension = 50
        else:
            self._dimension = dimension
        self._carte = [[0 for j in range(dimension)] for i in range(dimension)]
        for i in range(dimension):
            for j in range(dimension):
                if randint(1,2) == 1:
                    self._carte[i][j] = self._duree_repousse
                else:
                    self._carte[i][j] = randint(0, self._duree_repousse-1)

    def herbe_pousse(self):
        """
        Fais pousser l'herbe de la carte
        Données: Aucuns paramètre pour cette méthode
        Résultat: Augmente chaque coefficient de la carte de 1, ne renvoie rien
        """
        for i in range(self._dimension):
            for j in range(self._dimension):
                self._carte[i][j] += 1

    def herbe_mangee(self, i, j):
        """
        Renvoie le status de l'herbe à une position donnée
        Données:
            i : entier positif ou nul, abscisse dans la matrice
            j : entier positif ou nul, ordonnée dans la matrice
        Résultat:
            Renvoie un booléen, Vraie si l'herbe est en dessous de la durée de repousse
                                Faux si l'herbe est au dessus de la durée de repousse
        """
        if self._carte[i][j] < self._duree_repousse:
            return True
        return False

    def nb_herbe(self):
        """
        Renvoie le nombre de carré d'herbe poussés
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier positif, nombre de carré d'herbe poussés
        """
        compte_herbe = 0
        for lignes in self._carte:
            for colonnes in lignes:
                if colonnes >= self._duree_repousse:
                    compte_herbe += 1
        return compte_herbe

    def get_coef_carte(self, i ,j):
        """
        Renvoi un coefficient de la matrice
        Données: 
            i : entier positif ou nul, abscisse dans la matrice
            j : entier positif ou nul, ordonnée dans la matrice
        Résultat:
            Renvoie un entier, coefficient de la matrice à une position donnée
        """
        return self._carte[i][j]

    def set_coef_carte(self, i, j, coeff):
        """
        Change un coefficient de la matrice
        Données:
            i : entier positif ou nul, abscisse dans la matrice
            j : entier positif ou nul, ordonnée dans la matrice
        Résultat:
            Change le coefficient de la matrice à une position donnée, ne renvoie rien
        """
        self._carte[i][j] = coeff

    def get_dimension(self):
        """
        Renvoi les dimension de la carte
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier, dimension de la carte
        """
        return self._dimension

    def get_carte(self):
        """
        Renvoi la carte
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie une liste, matrice des coefficients de la carte
        """
        return self._carte
