from random import random, randint, shuffle


class GeneticAlgorithm:

    def __init__(self):
        
        self.generation = []
        self.population = 10
        self.mutation_rate = 0.1
    

    def seed(self):
        pass


    def fitness(self, *args):
        return 0.5


    def reproduce(self):

        if len(self.generation)<1:
            print("Seed first.")
            return
        
        evaluations = []
        for genome in self.generation:
            evaluations.append(self.fitness(*genome))

        total = sum(evaluations)
        next_generation = []

        while len(next_generation) != self.population:
            for genome, evaluation in zip(self.generation, evaluations):
                if evaluation/total > random():
                    next_generation.append(genome)
                    break
        
        print("Generation: ", *self.generation)
        print("Average: ", sum(evaluations)/len(evaluations))
        print("Max sample: ", max(evaluations), self.generation[evaluations.index(max(evaluations))])

        self.generation = self.mutation(self.crossover(next_generation))
        
        print("Next Generation: ", *self.generation) 
        print()

        
    def crossover(self, pre_crossover):
        
        post_crossover = []

        while pre_crossover !=[]:

            shuffle(pre_crossover)
            mummy = pre_crossover.pop()
            daddy = pre_crossover.pop()
            post_crossover.append([mummy[0], daddy[1]])
            post_crossover.append([daddy[0], mummy[1]])
            shuffle(pre_crossover)
        
        return post_crossover


    def mutation(self, generation):
        
        return generation
