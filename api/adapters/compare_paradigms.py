import timeit
import matplotlib.pyplot as plt
import numpy as np

def factorize_procedural(number):
    factors = []
    i = 2
    while i <= number:
        if number % i == 0:
            factors.append(i)
            number = number / i
        else:
            i += 1
    return factors

def factorize_functional(number):
    def factorize_recursive(n, i, factors):
        if n == 1:
            return factors
        elif n % i == 0:
            return factorize_recursive(n / i, i, factors + [i])
        else:
            return factorize_recursive(n, i + 1, factors)
    return factorize_recursive(number, 2, [])

def compare_execution_time(n):
    number = n

    times = [
        ('Procedural', timeit.timeit(lambda: factorize_procedural(number), number=10)),
        ('Functional', timeit.timeit(lambda: factorize_functional(number), number=10))
    ]

    # Plotar gráfico de barras para comparar o tempo de execução
    labels, values = zip(*times)
    plt.bar(labels, values)
    plt.xlabel('Abordagem')
    plt.ylabel('Tempo de execução (segundos)')
    plt.title('Comparação de Tempo de Execução')
    plt.show()

def update_big_o_plot(n):
    numbers = np.linspace(2, n, 100)
    procedural_times = []
    functional_times = []

    for number in numbers:
        procedural_time = timeit.timeit(lambda: factorize_procedural(number), number=10)
        functional_time = timeit.timeit(lambda: factorize_functional(number), number=10)
        procedural_times.append(procedural_time)
        functional_times.append(functional_time)

    plt.plot(numbers, procedural_times, label='Procedural')
    plt.plot(numbers, functional_times, label='Functional')
    plt.xlabel('Número')
    plt.ylabel('Tempo de execução (segundos)')
    plt.title('Comparação de Tempo de Execução (Big O Notation)')
    plt.legend()
    plt.show()
