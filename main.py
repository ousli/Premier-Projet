import sys
import pygame
import simulation
import monde

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Simulation')
icone = pygame.image.load('img/logo.png')
pygame.display.set_icon(icone)

police = pygame.font.SysFont('arlrdbd', 30)


monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(10, monde1)

mouton = pygame.image.load("img/mouton.png").convert_alpha()
mouton = pygame.transform.scale(mouton, (20 ,20))

loup = pygame.image.load("img/loup.png").convert_alpha()
loup = pygame.transform.scale(loup, (20 ,20))

herbe_0 = pygame.image.load("img/herbe-0.jpg")
herbe_0 = pygame.transform.scale(herbe_0, (20 ,20))
herbe_1 = pygame.image.load("img/herbe-1.jpg")
herbe_1 = pygame.transform.scale(herbe_1, (20 ,20))
herbe_2 = pygame.image.load("img/herbe-2.jpg")
herbe_2 = pygame.transform.scale(herbe_2, (20 ,20))


while game1.nb_mouton() != 0 or game1.nb_loup() != 0 :
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
                screen.blit(herbe_0, (i * 20, j * 20))

            elif monde1.get_coef_carte(i, j) > 10 and monde1.get_coef_carte(i,j) <= 20:
                screen.blit(herbe_1, (i * 20, j * 20))

            elif monde1.get_coef_carte(i, j) > 20:
                screen.blit(herbe_2, (i * 20, j * 20))

            if (i, j) in coo_mouton and (i, j) in coo_loup:
                screen.blit(mouton, (i * 20, j * 20))
                screen.blit(loup, (i * 20, j * 20))

            elif (i, j) in coo_mouton:
                screen.blit(mouton, (i * 20, j * 20))

            elif (i, j) in coo_loup:
                screen.blit(loup, (i * 20, j * 20))


    nb_mouton = police.render('Nb de mouton : ' + str(+ game1.nb_mouton()), True, 'red')
    nb_loup = police.render('Nb de loup : ' + str(+ game1.nb_loup()), True, 'red')
    nb_herbe = police.render('Nb d\'herbe : ' + str(monde1.nb_herbe()), True, 'red')
    #actualisation de la fenetre pygame
    screen.blit(nb_mouton, (10, 10))
    screen.blit(nb_loup, (10, 35))
    screen.blit(nb_herbe, (10, 60))

    pygame.display.flip()
    pygame.time.wait(250)

print('Simulation terminée !')
