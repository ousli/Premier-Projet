import sys
import pygame
import simulation
import monde

pygame.init()
screen = pygame.display.set_mode((750,750))

monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(10, monde1)

while game1.nb_mouton() != 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    game1.simulation(monde1)
    coo_mouton = [e.get_position() for e in game1.get_mouton()]
    coo_loup = [e.get_position() for e in game1.get_loup()]
    for i in range(monde1.get_dimension()):
        for j in range(monde1.get_dimension()):
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
    pygame.display.flip()
    pygame.time.wait(500)

print('Simulation terminée !')
