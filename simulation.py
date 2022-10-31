import mouton
from random import randint

class Simulation():
    def __init__(self, nombre_mouton, fin_du_monde, monde):
        self._nombre_mouton = nombre_mouton
        self._horloge = 0
        self._fin_du_monde = fin_du_monde
        self._moutons = []
        self._moutons = [mouton.Mouton(4, (randint(0,49), randint(0,49)), 10) for i in range(nombre_mouton)]
        self._monde = monde
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)            


    def simMouton(self, monde):
        self._horloge += 1
        # print('Tour n° ', self._horloge)
        self._monde.herbePousse()
        for e in self._moutons:
            if e.variationEnergie(monde) <= 0:
                self._moutons.remove(e)
            else:
                e.variationEnergie(monde)
                naissance = randint(1,100)
                if naissance <= e._taux_reproduction:
                    # print('Nouveau mouton : ', 4, e.get_position()[0], e.get_position()[1], 4)
                    # print('Nouveau mouton !')
                    self._moutons.append(mouton.Mouton(4, e.get_position(), 4))
                e.deplacement(monde)
            # print('Position X:', e.get_position()[0], 'Position Y:', e.get_position()[1],  'Energie ', e.variationEnergie(monde))
        self._resultats_herbe = monde.nbHerbe()
        self._resultats_moutons = len(self._moutons)
        # print(self._resultats_herbe, ' carrés d\'herbes')
        # print(self._resultats_moutons, ' mouton(s)')

    def getfinmonde(self):
        return self._fin_du_monde
    
    def getMouton(self):
        return self._moutons


    def nbMouton(self):
        return len(self._moutons)