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

    def herbePousse(self):
        for i in range(self._dimension):
            for j in range(self._dimension):
                self._carte[i][j]+=1
                # self.setCoefCarte(i, j, self._duree_repousse)
    
    def herbeMangee(self, i, j):
        if self._carte[i][j] == 0:
            return True
        else:
            return False

    def nbHerbe(self):
        nbherbe=0
        for e in self._carte:
            for f in e:
                if f != 'm':
                    if f > 0:
                        nbherbe+=1
        return nbherbe
    
    def getCoefCarte(self, i ,j):
        return self._carte[i][j]
    
    def setCoefCarte(self, i, j, coeff):
        self._carte[i][j] = coeff

    def getDimmension(self):
        return self._dimension

    def getDureeRepousse(self):
        return self._duree_repousse

    def getCarte(self):
        return self._carte
