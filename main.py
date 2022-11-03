import sys
import pygame
import simulation
import monde

pygame.init()
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption('Simulation')
icone = pygame.image.load('logo.png')
pygame.display.set_icon(icone)

police = pygame.font.SysFont('arlrdbd', 30)


monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(10, monde1)

while game1.nb_mouton() != 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    game1.simulation(monde1)
    #récupération des coordonnées de tout les moutons et de tout les loups
    coo_mouton = [e.get_position() for e in game1.get_mouton()]
    coo_loup = [e.get_position() for e in game1.get_loup()]
    for i in range(monde1.get_dimension()):
        for j in range(monde1.get_dimension()):
            # Affichage sur la fenetre pygame
            if monde1.get_coef_carte(i, j) >= 0 and monde1.get_coef_carte(i,j) <=10:
                pygame.draw.rect(screen, (153, 240, 132),
                                pygame.Rect(i * 15, j * 15, 15, 15))
            elif monde1.get_coef_carte(i, j) > 10 and monde1.get_coef_carte(i,j) <= 20:
                pygame.draw.rect(screen, (106, 168, 91),
                                pygame.Rect(i * 15, j * 15, 15, 15))
            elif monde1.get_coef_carte(i, j) > 20:
                pygame.draw.rect(screen, (67, 105, 58),
                                pygame.Rect(i * 15, j * 15, 15, 15))

            if (i, j) in coo_mouton and (i, j) in coo_loup:
                pygame.draw.rect(screen, (0, 0, 0),
                                pygame.Rect(i * 15, j * 15, 7.5, 7.5))
                pygame.draw.rect(screen, (255, 255, 255),
                                pygame.Rect(i * 15 + 7.5, j * 15, 7.5, 7.5))

                pygame.draw.rect(screen, (255, 255, 255),
                                pygame.Rect(i * 15, j * 15 + 7.5, 7.5, 7.5))
                pygame.draw.rect(screen, (0, 0, 0),
                                pygame.Rect(i * 15 + 7.5, j * 15 + 7.5, 7.5, 7.5))

            elif (i, j) in coo_mouton:
                pygame.draw.rect(screen, (255, 255, 255),
                                pygame.Rect(i * 15, j * 15, 15, 15))

            elif (i, j) in coo_loup:
                pygame.draw.rect(screen, (0, 0, 0),
                                pygame.Rect(i * 15, j * 15, 15, 15))

    nb_mouton = police.render('Nb de mouton : ' + str(+ game1.nb_mouton()), True, 'red')
    nb_loup = police.render('Nb de loup : ' + str(+ game1.nb_loup()), True, 'red')
    nb_herbe = police.render('Nb d\'herbe : ' + str(monde1.nb_herbe()), True, 'red')
    #actualisation de la fenetre pygame
    screen.blit(nb_mouton, (10, 10))
    screen.blit(nb_loup, (10, 35))
    screen.blit(nb_herbe, (10, 60))

    pygame.display.flip()
    pygame.time.wait(500)

print('Simulation terminée !')
