import random
import math
from tqdm import tqdm

def sorted_score(arr):
    # score based
    # - The number of sorted elements
    # - The number of unique elements
    value_score = 1
    unique_score = 0
    seen = {}
    for i in range(0,len(arr)):
        if not(arr[i] in seen):
            seen[arr[i]] = 1
            unique_score += 1
        for j in range(0,len(arr)):
            if i < j and arr[i] < arr[j]:
                value_score += 1
            elif i > j and arr[i] > arr[j]:
                value_score += 1

    return float(value_score)+float(unique_score)*9/float(len(arr))

def compute_fitness(pop):
    fitness_scores = []
    for chromosome in pop:
        fitness_scores.append(sorted_score(chromosome))
    total_score = sum(fitness_scores)
    normalized_fitness_scores = map(lambda x: x/total_score, fitness_scores)
    return normalized_fitness_scores

def selection(fitness_scores,population):
    f_and_p = sorted(zip(fitness_scores, population))
    acc_fitness = [f_and_p[0]]
    for i in range(1, len(f_and_p)):
        acc_fitness.append((acc_fitness[i-1][0] + f_and_p[i][0],f_and_p[i][1]))
    cut_off = random.random()
    selected = [x[1] for x in acc_fitness if x[0] > cut_off]
    if (len(selected) > 200):
        return selected[-200:]
    return selected

def crossover(population):
    new_population = population[:]
    for i in range(len(population)):
        for j in range(i+1,len(population)):
            crossover_point = random.randint(1, len(population)-1)
            child_1 = population[i][:crossover_point] + population[j][crossover_point:]
            child_2 = population[j][:crossover_point] + population[i][crossover_point:]
            new_population.append(child_1)
            new_population.append(child_2)
    return new_population

def mutation(population,mutation_rate):
    for chromosome in population:
        for i in range(1, len(chromosome)):
            if random.random() > mutation_rate:
                temp = chromosome[i]
                chromosome[i] = chromosome[i-1]
                chromosome[i-1] = temp
    return population

def create_initial_population(nums_to_sort, num_of_chromosomes):
    pop = []
    for i in range(num_of_chromosomes):
        new_chromosome = nums_to_sort[:]
        # Fisher Yates Shuffle
        for j  in range(len(nums_to_sort)-1,1,-1):
            r = random.randint(0, j)
            temp = new_chromosome[j]
            new_chromosome[j] = new_chromosome[r]
            new_chromosome[r] = temp
        pop.append(new_chromosome)
    return pop

def gen_sort(arr, num_of_chromosomes, mutation_rate):
    pop = create_initial_population(arr,num_of_chromosomes)
    last_fitness = 0
    current_fitness = 100
    while math.fabs(last_fitness - current_fitness) > 1e-7:
        last_fitness = current_fitness
        fitness =compute_fitness(pop)
        selected = selection(fitness, pop)
        co = crossover(selected)
        pop = mutation(co,mutation_rate)
        current_fitness = max(fitness)
    fitness = compute_fitness(pop)
    print(pop[fitness.index(max(fitness))], max(fitness))

gen_sort([2,10,1,7,5,6,3,4,9,8],10, 0.2)
