from random import randint

class Mouton():
    def __init__(self, gain_nourriture, position, energie):
        self._gain_nourriture = gain_nourriture
        self._position = position #tuple
        self._energie = energie
    
    def variationEnergie(self, monde):
        if monde.herbeMangee(self.get_position()[0], self.get_position()[1]) == True:
            self._energie -=  1
        else:
            self._energie += self._gain_nourriture
            monde.setCoefCarte(self.get_position()[0], self.get_position()[1], 0)
        return self.get_energie()


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

    def get_gain_nourriture(self):
        return self._gain_nourriture

    def get_position(self):
        return self._position
    
    def set_position(self, i ,j):
        self._position = (i, j)
    
    def set_energie(self, energie):
        self._energie = energie

    def get_energie(self):
        return self._energie