from random import randint

class Loup():
    def __init__(self, gain_nourriture, position, energie):
        self._gain_nourriture = gain_nourriture
        self._position = position
        # self._energie = randint(1, 2*self._gain_nourriture)
        self._energie = energie

    def variationEnergie(self, simulation):
        for e in simulation.getMouton():
            if e.get_position() == self._position:
                simulation.getMouton().remove(e)
                self._energie += self._gain_nourriture
                # self.set_energie(self.get_energie() + self._gain_nourriture)
                return self._energie
        self._energie -= 1
        return self._energie

    def deplacement(self , monde, simulation):
        distance = randint(8,15)
        for e in simulation.getMouton():
            distance_x, distance_y = e.get_position()[0] - self._position[0], e.get_position()[1] - self._position[1]
            if distance_x >= -distance and distance_x <= distance:
                if distance_y >= -distance and distance_y <= distance:
                    if distance_x < 0:
                        i = -1
                    elif distance_x > 0:
                        i = 1
                    else:
                        i = 0
                    if distance_y < 0:
                        j = -1
                    elif distance_y > 0:
                        j = 1
                    else:
                        j = 0

                    i += self.get_position()[0]
                    j += self.get_position()[1]
                    self.set_position(i , j)
                    return
           
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