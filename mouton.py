from math import radians
from random import randint
import re

class Mouton():
    def __init__(self, gain_nourriture, position, taux_reproduction):
        self._gain_nourriture = gain_nourriture
        self._position = position #tuple
        self._energie = randint(1, 2*self._gain_nourriture)
        self._taux_reproduction = taux_reproduction
    
    def variationEnergie(self, monde):
        # on veut récupérer la position du mouton et la comparer avec le coefficent de la carte à cet endroit la
        # self.get_position()
        if monde.herbeMangee(self.get_position()[0], self.get_position()[1]) == True:
            self._energie -= 1
        else:
            self._energie += self._gain_nourriture
        return self._energie


    def deplacement(self , monde):
        self.get_position()
        i, j = randint(-1,1), randint(-1,1)

        if i + self.get_position()[0] > monde.getDimension():
            i += self.get_position()%monde.getDimension()
        elif i + self.get_position()[0] < 0:
            i = monde.getDimension()

        if j + self.get_position()[1] > monde.getDimension():
            j +=  + self.get_position()%monde.getDimension()
        elif j + self.get_position()[1] < 0:
            j = monde.getDimension()
        
        self.set_position(i, j)


    def get_position(self, ):
        return self._position

    
    def set_position(self, i ,j):
        self._position = (i, j)