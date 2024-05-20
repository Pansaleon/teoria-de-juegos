import numpy as np

# Definición de los payoffs para cada combinación de estrategias
payoffs = {
    ("A", "A", "A"): (4000, 4000, 4000),
    ("A", "A", "B"): (6000, 3500, 3500),
    ("A", "A", "C"): (7000, 3000, 3000),
    ("A", "B", "A"): (3500, 6000, 3500),
    ("A", "B", "B"): (5000, 5000, 3000),
    ("A", "B", "C"): (6000, 4500, 2500),
    ("A", "C", "A"): (3000, 7000, 3000),
    ("A", "C", "B"): (4000, 6000, 2500),
    ("A", "C", "C"): (5000, 5000, 2000),
    ("B", "A", "A"): (3500, 4000, 6000),
    ("B", "A", "B"): (5000, 3500, 5000),
    ("B", "A", "C"): (6000, 3000, 4500),
    ("B", "B", "A"): (3000, 6000, 6000),
    ("B", "B", "B"): (4000, 5000, 5000),
    ("B", "B", "C"): (5000, 4500, 4000),
    ("B", "C", "A"): (2500, 7000, 4500),
    ("B", "C", "B"): (3000, 6000, 4000),
    ("B", "C", "C"): (4000, 5000, 3500),
    ("C", "A", "A"): (3000, 4000, 7000),
    ("C", "A", "B"): (4500, 3500, 6000),
    ("C", "A", "C"): (5000, 3000, 5000),
    ("C", "B", "A"): (2500, 6000, 7000),
    ("C", "B", "B"): (3000, 5000, 6000),
    ("C", "B", "C"): (4000, 4500, 5000),
    ("C", "C", "A"): (2000, 7000, 6000),
    ("C", "C", "B"): (2500, 6000, 5000),
    ("C", "C", "C"): (3000, 5000, 4000),
}

# Definir las estrategias posibles
strategies = ["A", "B", "C"]

# Encontrar el equilibrio de Nash
def is_nash_equilibrium(strategy_combination):
    juan_strategy, pedro_strategy, luis_strategy = strategy_combination
    juan_payoff = payoffs[(juan_strategy, pedro_strategy, luis_strategy)][0]
    pedro_payoff = payoffs[(juan_strategy, pedro_strategy, luis_strategy)][1]
    luis_payoff = payoffs[(juan_strategy, pedro_strategy, luis_strategy)][2]

    # Revisar si Juan puede mejorar su payoff cambiando su estrategia
    for juan in strategies:
        if payoffs[(juan, pedro_strategy, luis_strategy)][0] > juan_payoff:
            return False

    # Revisar si Pedro puede mejorar su payoff cambiando su estrategia
    for pedro in strategies:
        if payoffs[(juan_strategy, pedro, luis_strategy)][1] > pedro_payoff:
            return False

    # Revisar si Luis puede mejorar su payoff cambiando su estrategia
    for luis in strategies:
        if payoffs[(juan_strategy, pedro_strategy, luis)][2] > luis_payoff:
            return False

    return True

# Buscar y mostrar todos los equilibrios de Nash
nash_equilibria = []
for juan in strategies:
    for pedro in strategies:
        for luis in strategies:
            if is_nash_equilibrium((juan, pedro, luis)):
                nash_equilibria.append((juan, pedro, luis))

print("Equilibrios de Nash encontrados:")
for equilibrium in nash_equilibria:
    print(f"Estrategia de Juan: {equilibrium[0]}, Estrategia de Pedro: {equilibrium[1]}, Estrategia de Luis: {equilibrium[2]}")
    print(f"Payoffs: {payoffs[equilibrium]}")