import random
import math
import matplotlib.pyplot as plt
import numpy as np

def fitness(x):
    return x * math.sin(10 * math.pi * x) + 1.0

def mutate(x, rate=0.1):
    if random.random() < rate:
        x += random.uniform(-0.1, 0.1)
        x = max(0, min(1, x))
    return x

def crossover(a, b):
    alpha = random.random()
    return alpha * a + (1 - alpha) * b

def evolve(pop_size=50, generations=60):
    population = [random.random() for _ in range(pop_size)]

    # Prepare plot
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Precompute the fitness curve
    xs = np.linspace(0, 1, 400)
    ys = [fitness(x) for x in xs]
    max_y = max(ys) + 0.2

    for g in range(generations):
        ax.clear()
        ax.set_title(f"Evolution — Generation {g}")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, max_y)

        # Draw fitness function
        ax.plot(xs, ys, linewidth=2)

        # Draw population on their actual fitness positions
        ax.scatter(population, [fitness(x) for x in population], s=30)

        plt.pause(0.1)

        # Selection
        scored = [(fitness(x), x) for x in population]
        scored.sort(reverse=True)
        population = [x for _, x in scored]

        elites = population[:5]
        total_fit = sum(f for f, _ in scored)

        def pick():
            r = random.uniform(0, total_fit)
            s = 0
            for f, x in scored:
                s += f
                if s >= r:
                    return x

        new_pop = elites[:]
        while len(new_pop) < pop_size:
            p1, p2 = pick(), pick()
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    plt.ioff()
    plt.show()

    return population

final_population = evolve()

