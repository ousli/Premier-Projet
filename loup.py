from random import randint

class Loup():
    def __init__(self, gain_nourriture, position, taux_reproduction):
        self._gain_nourriture = gain_nourriture
        self._position = position
        self._energie = randint(1, 2*self._gain_nourriture)
        self._taux_reproduction = taux_reproduction

    def variationEnergie(self, simulation):
            for e in simulation.getMouton():
                if e.get_position() == self._position:
                    simulation.getMouton().remove(e)
            return self._energie

    def deplacement(self , monde):
            i, j = randint(-1,1), randint(-1,1)
            i += self.get_position()[0]
            j += self.get_position()[1]

            if i > monde.getDimension()-1:
                i = 0
            else:
                if i < 0:
                    i = monde.getDimension()-1

            if j > monde.getDimension()-1:
                j = 0
            else:
                if j  < 0:
                    j = monde.getDimension()-1
            
            self.set_position(i, j)

    def get_position(self):
        return self._position

            
    def set_position(self, i ,j):
        self._position = (i, j)   
    
    def get_taux_reproduction(self):
        return self._taux_reproduction