import random

# Example: maximize f(x) = x*sin(10*pi*x) + 1.0
# Domain: x in [0, 1]

def fitness(x):
    import math
    return x * math.sin(10 * math.pi * x) + 1.0

def mutate(x, rate=0.1):
    if random.random() < rate:
        x += random.uniform(-0.1, 0.1)
        x = max(0, min(1, x))  # keep in bounds
    return x

def crossover(a, b):
    alpha = random.random()
    return alpha * a + (1 - alpha) * b

def evolve(pop_size=50, generations=200):
    population = [random.random() for _ in range(pop_size)]

    for _ in range(generations):
        scored = [(fitness(x), x) for x in population]
        scored.sort(reverse=True)
        population = [x for _, x in scored]

        # Keep elites
        elites = population[:5]

        # Select parents proportional to fitness
        total_fit = sum(f for f, _ in scored)
        def pick():
            r = random.uniform(0, total_fit)
            s = 0
            for f, x in scored:
                s += f
                if s >= r:
                    return x

        # Breed new generation
        new_pop = elites[:]
        while len(new_pop) < pop_size:
            p1, p2 = pick(), pick()
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    best = max(population, key=fitness)
    return best, fitness(best)

best_x, best_score = evolve()
print("Best x:", best_x)
print("Best score:", best_score)

