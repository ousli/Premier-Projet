import monde, mouton
from random import randint

class Simulation():
    def __init__(self, nombre_mouton, fin_du_monde, monde):
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._fin_du_monde = fin_du_monde
        self._moutons = []
        self._moutons = [mouton.Mouton(4, (randint(0,50), randint(0,50)), 4) for i in range(nombre_mouton)]
        self._monde = monde
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)
        # for i in range(self._nombre_mouton):
        #     i, j = randint(0,50), randint(0,50)
        #     # verifier qu'il n'y a pas déjà un mouton à cet endroit
        #     for e in self._moutons:
        #         if e.get_position() != (i, j):
        #             self._moutons.append(mouton.Mouton(4, (i, j), 4))
            


    def simMouton(self, monde):
        self._horloge += 1
        print('Tour n° ', self._horloge)
        self._monde.herbePousse()
        for e in self._moutons:
            e.variationEnergie(monde)
            e.deplacement(monde)

    def getfinmonde(self):
        return self._fin_du_monde
    
    def getMouton(self):
        return self._moutons

    def nbMouton(self):
        nb = 0
        for e in self._moutons:
            nb+=1
        return nb