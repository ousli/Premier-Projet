import secrets
import sys
import simulation, monde
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((750,750))

monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(4, 10, monde1)

print('#######################################')
print('DEBUT DE LA PARTIE ')
for e in game1.getMouton():
     print('Position X:', e.get_position()[0], 'Position Y:', e.get_position()[1],  'Energie ', e.variationEnergie(monde1))
print('#######################################')


while game1.nbMouton() != 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# while i <= game1.getfinmonde(): 
    coo_mouton = [e.get_position() for e in game1.getMouton()]
    # print(coo_mouton)
    print('\n')
    game1.simMouton(monde1)
    x=0
    y=0
    for i in range(monde1.getDimension()):
        x=0
        ligne=''
        for j in range(monde1.getDimension()):
            if (i , j) in coo_mouton:
                ligne += '█'
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y,15,15))
            else:
                if monde1.getCoefCarte(i,j) >= 0 and monde1.getCoefCarte(i,j) <=10:
                    ligne += '░'
                    pygame.draw.rect(screen, (153, 240, 132), pygame.Rect(x,y,15,15))
                elif monde1.getCoefCarte(i,j) > 10 and monde1.getCoefCarte(i,j) <=20:
                    ligne += '▒'
                    pygame.draw.rect(screen, (106,168,91), pygame.Rect(x,y,15,15))
                elif monde1.getCoefCarte(i,j) > 20:
                    ligne += '▓'
                    pygame.draw.rect(screen, (67,105,58), pygame.Rect(x,y,15,15))
            x+=15
        y+=15
        print(ligne)
    pygame.display.flip()  
           

    i+=1
    time.sleep(0.5)

print('Simulation terminée !')


