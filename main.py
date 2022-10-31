import simulation, monde
import time

monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(4, 10, monde1)

i=1
# print(ord('░'), ord('▒'), ord('▓'))
# 9617 9618 9619
print('#######################################')
print('DEBUT DE LA PARTIE ')
for e in game1.getMouton():
     print('Position X:', e.get_position()[0], 'Position Y:', e.get_position()[1],  'Energie ', e.variationEnergie(monde1))
print('#######################################')

# for e in game1.getMouton():
#     e.get_position()
while game1.nbMouton() != 0:
# while i <= game1.getfinmonde(): 
    coo_mouton = [e.get_position() for e in game1.getMouton()]
    # print(coo_mouton)
    print('\n')
    game1.simMouton(monde1)
    for i in range(monde1.getDimension()):
        ligne=''
        for j in range(monde1.getDimension()):
            # print(monde1.getCarte()[i][j])
            if (i , j) in coo_mouton:
                ligne += '█'
            else:
                if monde1.getCoefCarte(i,j) >= 0 and monde1.getCoefCarte(i,j) <=10:
                    ligne += '░'
                elif monde1.getCoefCarte(i,j) > 10 and monde1.getCoefCarte(i,j) <=20:
                    ligne += '▒'
                elif monde1.getCoefCarte(i,j) > 20:
                    ligne += '▓'
        print(ligne)    
            

    i+=1
    time.sleep(0.5)

print('Simulation terminée !')


