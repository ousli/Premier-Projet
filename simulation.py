from random import randint
import mouton
import loup

class Simulation():
    """
    Classe qui gère la simulation

    Attributs:
        _nombre_mouton() : Entier positif, nombre de mouton dans la simulation
        _horloge() : Entier positif ou nul, nombre de tour de la simulation
        _moutons() : Liste, contient tout les objets moutons de la simulation
        _loups() : Liste, contient tout les objets loups de la simulation
        _monde() : Classe de type Monde dans laquel vas tournée la simulation
        _resultats_herbe() : Entier positif, nombre de carrés d'herbes poussés dans la simulation
        _resultats_moutons() : Entier positif ou nul, nombre de moutons dans la simulation
        _resultats_loups() : Entier positif ou nul, nombre de loups dans la simulation
    Méthodes:
        __init__() : Constructeur de la classe Simulation
        simulation() : Fais tournée la simulation
        get_mouton() : Renvoie la liste des moutons dans la simulation
        nb_mouton() : Renvoie le nombre de mouton dans la simulation
        get_loup() : Renvoie la liste des loups dans la simulation
        nb_loup() : Renvoie le nombre de loup dans la simulation
    """
    def __init__(self, nombre_mouton, monde):
        """
        Constructeur de la classe Simulation
        Données:
            _nombre_mouton() : Entier positif, nombre de mouton dans la simulation
            _horloge() : Entier positif ou nul, nombre de tour de la simulation
            _moutons() : Liste, contient tout les objets moutons de la simulation
            _loups() : Liste, contient tout les objets loups de la simulation
            _monde() : Classe de type Monde dans laquel vas tournée la simulation
            _resultats_herbe() : Entier positif,
                                nombre de carrés d'herbes poussés dans la simulation
            _resultats_moutons() : Entier positif ou nul, nombre de moutons dans la simulation
            _resultats_loups() : Entier positif ou nul, nombre de loups dans la simulation
        Résultat:
            Crée une nouvelle simulation, ne renvoie rien
        """
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._moutons = [mouton.Mouton(4, (randint(0,49), randint(0,49)),randint(4,8))
                            for i in range(nombre_mouton)]
        self._loups = [loup.Loup(19, (randint(0,49), randint(0,49)), 27)
                            for i in range(nombre_mouton // 2)]
        self._monde = monde
        self._resultats_herbe = monde.nb_herbe()
        self._resultats_moutons = self.nb_mouton()
        self._resultats_loups = self.nb_loup()


    def simulation(self, monde):
        """
        Fais tournée la simulation
        Données:
            monde: Objet de type monde dans laquel vas tournée la simulation
        Résultat:
            Augmente l'horloge
            Fait pousser l'herbe
            Change l'énergie des moutons et des loups, les tuant si ils n'en ont plus
            Fais se reproduire les moutons et les loups
            Compte le nombre de carrés d'herbe poussés, de mouton et de loup
            Ne renvoie rien
        """
        self._horloge += 1
        self._monde.herbe_pousse()
        for single_loup in self._loups:
            single_loup.variation_energie(self)
            if single_loup.get_energie() <= 0:
                self._loups.remove(single_loup)
            else:
                if single_loup.get_energie() >= single_loup.get_gain_nourriture() * 2.5:
                    self._loups.append(loup.Loup(19, single_loup.get_position(),
                                                    single_loup.get_energie() // 2))
                    single_loup.set_energie(single_loup.get_energie() // 2)
                single_loup.deplacement(monde, self)
        for single_mouton in self._moutons:
            single_mouton.variation_energie(monde)
            if single_mouton.get_energie() <= 0:
                self._moutons.remove(single_mouton)
            else:
                if single_mouton.get_energie() >= single_mouton.get_gain_nourriture() * 10:
                    self._moutons.append(mouton.Mouton(4, single_mouton.get_position(),
                                                        single_mouton.get_energie()//2))
                    single_mouton.set_energie(single_mouton.get_energie() // 2)
                single_mouton.deplacement(monde)

        self._resultats_herbe = monde.nb_herbe()
        self._resultats_moutons = self.nb_mouton()
        self._resultats_loups = self.nb_loup()

    def get_mouton(self):
        """
        Renvoie la liste des moutons dans la simulation
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie une liste, contenant les moutons de la simulation
        """
        return self._moutons

    def nb_mouton(self):
        """
        Renvoie le nombre de mouton dans la simulation
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier positif ou nul, nombre de moutons dans la simulation
        """
        return len(self._moutons)

    def get_loup(self):
        """
        Renvoie la liste des loups dans la simulation
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie une liste, contenant les loups de la simulation
        """
        return self._loups

    def nb_loup(self):
        """
        Renvoie le nombre de loup dans la simulation
        Données: Aucuns paramètre pour cette méthode
        Résultat: Renvoie un entier positif ou nul, nombre de loups dans la simulation
        """
        return len(self._loups)
        