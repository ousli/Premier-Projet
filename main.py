import simulation, monde
import time

monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(4, 10, monde1)

i=1
while i <= game1.getfinmonde():
    game1.simMouton(monde1)
    print(game1.getMouton())
    for e in game1.getMouton():
        print(e.get_position(), e.variationEnergie(monde1))
    print(monde1.nbHerbe())
    i+=1
    time.sleep(1)
print('Simulation terminée !')