import simulation, monde
import time

monde1 = monde.Monde(50, 30)
game1 = simulation.Simulation(4, 10, monde1)

i=1
for e in game1.getMouton():
    print('Position X:', e.get_position()[0], 'Position Y:', e.get_position()[1],  'Energie ', e.variationEnergie(monde1))


while i <= game1.getfinmonde(): 
    game1.simMouton(monde1)
    i+=1
    time.sleep(1)
print('Simulation terminée !')