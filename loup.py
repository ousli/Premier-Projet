from random import randint
import animaux

class Loup(animaux.Animaux):
    """
    Animal de type loup, pour une simulation
    Hérite de la classe Animaux

    Méthodes:
        __init__(): Constructeur de la classe Loup
        variation_energie() : Fais varier l'énergie du loup si
                            il est sur une case avec de l'herbe ou avec un mouton
        deplacement : Fais se déplacer le loup
    """
    def __init__(self, gain_nourriture, position, energie):
        """
        Constructeur de la classe Loup
        Données:
            Attribut de la classe Animaux
        Résultat:
            Crée un nouveau loup, ne renvoie rien
        """
        animaux.Animaux.__init__(self, gain_nourriture, position, energie)

    def variation_energie(self, simulation):
        """
        Fais varier l'énergie du loup si
                    il est sur une case avec de l'herbe ou avec un mouton
        Données:
            simulation: Objet de type simulation qui contient la liste des moutons
        Résultat:
            Enlève de l'énergie au loup si il est sur de l'herbe,
            lui en ajoute si il est sur la même case qu'un mouton.
            Renvoi l'energie qu'il lui reste
        """
        for mouton in simulation.get_mouton():
            if mouton.get_position() == self._position:
                simulation.get_mouton().remove(mouton)
                self._energie += self._gain_nourriture
                return self._energie
        self._energie -= 1
        return self._energie

    def deplacement(self, monde, simulation):
        """
        Fais se déplacer le loup
        Données:
            monde: Objet de type monde, matrice dans lequel se trouve l'animal
            simulation : Objet de type simulation qui contient la liste des moutons
        Résultat:
            Déplace le loup vers un mouton si il y en a un dans un rayon
            aléatoire compris en 8 et 15 cases autour de lui, sinon le déplace
            aléatoirement. Ne renvoie rien
        """
        distance = randint(8, 15)
        for mouton in simulation.get_mouton():
            (distance_x, distance_y) = (mouton.get_position()[0] - self._position[0],
                                        mouton.get_position()[1] - self._position[1])
            if distance_x >= -distance and distance_x <= distance:
                if distance_y >= -distance and distance_y <= distance:
                    if distance_x < 0:
                        i = -1
                    elif distance_x > 0:
                        i = 1
                    else:
                        i = 0
                    if distance_y < 0:
                        j = -1
                    elif distance_y > 0:
                        j = 1
                    else:
                        j = 0

                    i += self.get_position()[0]
                    j += self.get_position()[1]
                    self.set_position(i, j)
                    return
        super().deplacement(monde)
        