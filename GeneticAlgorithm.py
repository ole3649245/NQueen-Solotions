#GeneticAlgorithmSrisanNatthawan
import random
import time

def fitness_function(solution, N):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if solution[i] != solution[j] and abs(solution[i] - solution[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parents = random.choices(population, probabilities, k=2)
    return parents

def crossover(parent1, parent2, N):
    crossover_point = random.randint(0, N - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(child, N, mutation_rate):
    if random.random() < mutation_rate:
        index = random.randint(0, N - 1)
        child[index] = random.randint(0, N - 1)
    return child

def genetic_algorithm(N, population_size=100, generations=1000, mutation_rate=0.1):
    population = [[random.randint(0, N - 1) for _ in range(N)] for _ in range(population_size)]
    
    for generation in range(generations):
        fitness_scores = [fitness_function(individual, N) for individual in population]
        if max(fitness_scores) == N * (N - 1) // 2:  # All pairs are non-attacking
            solution = population[fitness_scores.index(max(fitness_scores))]
            return solution, generation
        
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2, N)
            child = mutate(child, N, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    # Return best solution found
    best_fitness = max(fitness_scores)
    best_solution = population[fitness_scores.index(best_fitness)]
    return best_solution, generations

# Test for N=10
N = 10
start_time = time.time()
solution, generations = genetic_algorithm(N)
end_time = time.time()

print(f"Solution for N={N}: {solution}")
print(f"Generations taken: {generations}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
