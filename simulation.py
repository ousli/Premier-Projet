import mouton, loup
from random import randint

class Simulation():
    def __init__(self, nombre_mouton, fin_du_monde, monde):
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._fin_du_monde = fin_du_monde
        self._moutons = []
        self._moutons = [mouton.Mouton(4, (randint(0,49), randint(0,49)), randint(4,8)) for i in range(nombre_mouton)]
        self._loups = [loup.Loup(19, (randint(0,49), randint(0,49)), 27) for i in range(nombre_mouton//2)]
        self._monde = monde
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)            


    def simMouton(self, monde):
        self._horloge += 1
        self._monde.herbePousse()
        for e in self._moutons:
            e.variationEnergie(monde)
            if e.get_energie() <= 0:
                self._moutons.remove(e)
            else:
                if e.get_energie() >= e.get_gain_nourriture() * 10:
                    self._moutons.append(mouton.Mouton(4, e.get_position(), e.get_energie()//2))
                    e.set_energie(e.get_energie()//2)
                e.deplacement(monde)
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)

    def simLoup(self, monde):
        for e in self._loups:
            e.variationEnergie(self)
            if e.get_energie() <= 0:
                self._loups.remove(e)
            else:
                if e.get_energie() >= e.get_gain_nourriture() * 2.5:
                    self._loups.append(loup.Loup(19, e.get_position(), e.get_energie()//2))
                    e.set_energie(e.get_energie()//2)
                e.deplacement(monde, self)

    def getfinmonde(self):
        return self._fin_du_monde
    
    def getMouton(self):
        return self._moutons

    def nbMouton(self):
        return len(self._moutons)
    
    def getLoup(self):
        return self._loups