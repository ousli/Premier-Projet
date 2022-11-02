from random import randint
import animaux

class Mouton(animaux.Animaux):
    def __init__(self, gain_nourriture, position, energie):
        animaux.Animaux.__init__(self,gain_nourriture,position,energie)
    
    def variationEnergie(self, monde):
        if monde.herbeMangee(self.get_position()[0], self.get_position()[1]) == True:
            self._energie -=  1
        else:
            self._energie += self._gain_nourriture
            monde.setCoefCarte(self.get_position()[0], self.get_position()[1], 0)
        return self._energie