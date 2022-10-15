import mouton
from random import randint

class Simulation():
    def __init__(self, nombre_mouton, fin_du_monde, monde):
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._fin_du_monde = fin_du_monde
        self._moutons = []
        self._moutons = [mouton.Mouton(4, (randint(0,49), randint(0,49)), 4) for i in range(nombre_mouton)]
        self._monde = monde
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)            


    def simMouton(self, monde):
        self._horloge += 1
        print('Tour n° ', self._horloge)
        self._monde.herbePousse()
        for e in self._moutons:
            print('Position X:', e.get_position()[0], 'Position Y:', e.get_position()[1],  'Energie ', e.variationEnergie(monde))
            e.variationEnergie(monde)
            if e.variationEnergie(monde) <= 0:
                self._moutons.remove(e)
            else:
                if randint(1,100) <= e._taux_reproduction:
                    print('Nouveau mouton : ', 4, e.get_position()[0], e.get_position()[1], 4)
                    self._moutons.append(mouton.Mouton(4, e.get_position(), 4))
            e.deplacement(monde)
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)
        print(self._resultats_herbe)
        print(self._resultats_moutons)

    def getfinmonde(self):
        return self._fin_du_monde
    
    def getMouton(self):
        return self._moutons

    def nbMouton(self):
        # nb = 0
        # for e in self._moutons:
        #     nb+=1
        # return nb
        return len(self._moutons)