from random import randint
import animaux

class Loup(animaux.Animaux):
    def __init__(self, gain_nourriture, position, energie):
        animaux.Animaux.__init__(self,gain_nourriture,position,energie)

    def variationEnergie(self, simulation):
        for e in simulation.getMouton():
            if e.get_position() == self._position:
                simulation.getMouton().remove(e)
                self._energie += self._gain_nourriture
                return self._energie
        self._energie -= 1
        return self._energie

    def deplacement(self, monde, simulation):
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
        super().deplacement(monde)