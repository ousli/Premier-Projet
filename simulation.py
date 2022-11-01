import mouton, loup
from random import randint

class Simulation():
    def __init__(self, nombre_mouton, fin_du_monde, monde):
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._fin_du_monde = fin_du_monde
        self._moutons = []
        self._moutons = [mouton.Mouton(4, (randint(0,49), randint(0,49)), 4) for i in range(nombre_mouton)]
        self._loups = [loup.Loup(19, (randint(0,49), randint(0,49)), 5) for i in range(nombre_mouton//2)]
        self._monde = monde
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)            


    def simMouton(self, monde):
        self._horloge += 1
        self._monde.herbePousse()
        for e in self._moutons:
            if e.variationEnergie(monde) <= 0:
                self._moutons.remove(e)
            else:
                e.variationEnergie(monde)
                naissance = randint(1,100)
                if naissance <= e.get_taux_reproduction():
                    self._moutons.append(mouton.Mouton(4, e.get_position(), 4))
                e.deplacement(monde)
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)
    def simLoup(self, monde):
        for e in self._loups:
            if  e.variationEnergie(self) <= 0:
                self._loups.remove(e)
            else:
                e.variationEnergie(self)
                naissance = randint(1,100)
                if naissance <= e.get_taux_reproduction():
                    self._loups.append(loup.Loup(19, e.get_position(), 5))
                e.deplacement(monde)

    def getfinmonde(self):
        return self._fin_du_monde
    
    def getMouton(self):
        return self._moutons

    def nbMouton(self):
        return len(self._moutons)
    
    def getLoup(self):
        return self._loups