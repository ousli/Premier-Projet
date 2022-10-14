from random import randint

class Monde():
    # dimension => taille du monde
    # duree_repousse =>
    # 
    def __init__(self, dimension, duree_repousse):
        
        self._duree_repousse = duree_repousse
        if dimension < 50:
            self._dimension = 50
        else:
            self._dimension = dimension
        self._carte = [[0 for j in range(dimension)] for i in range(dimension)]
        for i in range(dimension):
            for j in range(dimension):
                if randint(1,2) == 1:
                     self._carte[i][j] = self._duree_repousse
                else:
                    self._carte[i][j] = randint(0, self._duree_repousse-1)
                    #on met une valeur entre 0 et durée repousse




    def herbePousse(self):
        for i in range(self._dimension):
            for j in range(self._dimension):
                self._carte[i][j]+=1
                # self.setCoefCarte(i, j, self._duree_repousse)
    
    def herbeMangee(self, i, j):
        if self._carte[i][j] < self._duree_repousse:
            return True
        else:
            return False

    def nbHerbe(self):
        nbherbe=0
        for e in self._carte:
            for f in e:
                if f >= self._duree_repousse:
                    nbherbe+=1
        return nbherbe
    
    def getCoefCarte(self, i ,j):
        return self._carte[i][j]
    
    def setCoefCarte(self, i, j, coeff):
        self._carte[i][j] = coeff

    def getDimension(self):
        return self._dimension

    def getDureeRepousse(self):
        return self._duree_repousse

    def getCarte(self):
        return self._carte
