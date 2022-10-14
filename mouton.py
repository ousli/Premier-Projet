from random import randint

class Mouton():
    def __init__(self, gain_nourriture, position, taux_reproduction):
        self._gain_nourriture = gain_nourriture
        self._position = position #tuple
        self._energie = randint(1, 2*self._gain_nourriture)
        self._taux_reproduction = taux_reproduction
    
    def variationEnergie(self):
        
        return self._energie


    def deplacement(self):
        return


    def get_position(self):
        return self._position

        #on veut récupérer la position du mouton et la comparer avec le coefficent de la carte à cet endroit la
    
    def set_position(self, i ,j):
        self._position = (i, j)