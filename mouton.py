import animaux

class Mouton(animaux.Animaux):
    """
    Animal de type mouton, pour une simulation
    Hérite de la classe Animaux

    Méthodes:
        __init__(): Constructeur de la classe Mouton
        variation_energie() : Fais varier l'énergie du mouton si
                            il est sur une case avec de l'herbe
    """
    def __init__(self, gain_nourriture, position, energie):
        """
        Constructeur de la classe Mouton
        Données:
            Attribut de la classe Animaux
        Résultat:
            Crée un nouveau mouton, ne renvoie rien
        """
        animaux.Animaux.__init__(self,gain_nourriture,position,energie)

    def variation_energie(self, monde):
        """
        Fais varier l'énergie du mouton si
                    il est sur une case avec de l'herbe
        Données:
            monde: Objet de type Monde qui contient la matrice des coefficients de pousse de l'herbe
        Résultat:
            Enlève de l'énergie au mouton si il est sur une case d'herbe qui n'a pas poussée
            Lui en ajoute si il est sur une case avec de l'herbe poussée
            Renvoi l'energie qu'il lui reste
        """
        if monde.herbe_mangee(self.get_position()[0], self.get_position()[1]) is True:
            self._energie -=  1
        else:
            self._energie += self._gain_nourriture
            monde.set_coef_carte(self.get_position()[0], self.get_position()[1], 0)
        return self._energie
