import AntCLASS
import random
ants.append([random.randint(0,50),random.randint(0,50)])

for i in range(number_of_ants):
    ants.append(AntCLASS.Ant([]))
ant = ants[0]

while ants is not empty:
    ant.move()
    ant.age()
    if ant.lifetime == 0:
        ants.remove(ant)

    if ant.position == food.position:
        ant.