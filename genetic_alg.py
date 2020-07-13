import random

from pyeasyga import pyeasyga
from pyeasyga.pyeasyga import Chromosome

from main import *

desired = 50000
mr = [int(desired / 2)]

data = [desired] * length * 5
ga = pyeasyga.GeneticAlgorithm(data,
                               population_size=200,
                               generations=100000,
                               mutation_probability=1,
                               crossover_probability=0.00,
                               elitism=False,
                               maximise_fitness=False)


def mutate(individual):
    if mr[0] == 0:
        mr[0] = 1
    for _ in range(16):
        mutate_index = random.randrange(len(individual))
        val = individual[mutate_index] + random.randrange(-mr[0], mr[0])
        if val < 0:
            val = 0
        individual[mutate_index] = val


# define and set function to create a candidate solution representation
def create_individual(data):
    return [random.randrange(0, desired) for i in range(length * length)]


ga.create_individual = create_individual
ga.mutate_function = mutate
ga.fitness_function = fitness  # set the GA's fitness function


def run():
    """Run (solve) the Genetic Algorithm."""
    ga.create_first_generation()
    prev = ''
    removing = 0

    for i in range(1, ga.generations):
        ga.create_next_generation()
        mr[0] = int(ga.best_individual()[0] / 5)
        if ga.best_individual()[0] == 0:
            return ga.best_individual()
        if i % 10 == 0:
            print(i, ga.best_individual())
        if prev == ga.best_individual():
            removing += 1
            # for j in range(10):
            #     ga.current_generation[j] = Chromosome(create_individual(data))
        if removing > 5:
            removing = 0
            print("removing")

            for j in range(int(20)):
                ga.current_generation[j] = Chromosome(create_individual(data))
        prev = ga.best_individual()


print(run())
