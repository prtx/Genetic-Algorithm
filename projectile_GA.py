from random import random, randint, shuffle

from genetic_algorithm import GeneticAlgorithm
from projectile import tt, screen, projectile, projectile_with_block, build_block, x_offset, y_offset


class ProjectileGA(GeneticAlgorithm):

    def seed(self):
        for i in range(self.population):
            self.generation.append([randint(0, 100), randint(0, 90)])
    
    
    def mutation(self, generation):
        
        for genome in generation:
            if random() <= self.mutation_rate:
                genome[0] = randint(0, 100)
            if random() <= self.mutation_rate:
                genome[1] = randint(0, 90)

        return generation


class ProjectileDistanceGA(ProjectileGA):

    def fitness(self, *args):
        return projectile_with_block(*args, gfx=True)

    
def projectile_with_distance():
    a = ProjectileDistanceGA()
    a.seed()
    while True:
        build_block(100, 0, 50)
        build_block(100, 100, 50)
        build_block(100, 200, 50)
        a.reproduce()
        screen.reset()


class ProjectilePositionGA(ProjectileGA):

    x = 0
    
    def fitness(self, *args):
        y = projectile(*args, gfx=True)
        print(y, args)
        return 1000 - abs(y - self.x)

    
def projectile_with_position(x):
    a = ProjectilePositionGA()
    a.x = x
    a.seed()
    while True:
        tt.penup()
        tt.goto(x_offset+x, y_offset)
        tt.pendown()
        tt.circle(5)
        a.reproduce()
        screen.reset()

if __name__ == '__main__':
    projectile_with_distance()
    # projectile_with_position(100)
