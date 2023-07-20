import timeit
import matplotlib.pyplot as plt

def factorize_procedural(n):
    factors = []

    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n //= i

    return factors

def factorize_functional(n):
    factors = []

    divide = lambda d: factors.append(d) and factorize_functional(n//d) if n % d == 0 else None

    divide(2)

    for i in range(3, int(n**0.5)+1, 2):
        divide(i)

    if n > 2:
        factors.append(n)

    return factors

def compare_execution_time():
    number = 1000000

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

def compare_big_o_notation():
    numbers = list(range(2, 100))
    big_o_procedural = []
    big_o_functional = []

    for number in numbers:
        time_procedural = timeit.timeit(lambda: factorize_procedural(number), number=10)
        time_functional = timeit.timeit(lambda: factorize_functional(number), number=10)

        big_o_procedural.append(time_procedural)
        big_o_functional.append(time_functional)

    # Plotar gráfico de linha para comparar a notação Big O
    plt.plot(numbers, big_o_procedural, label='Procedural')
    plt.plot(numbers, big_o_functional, label='Functional')
    plt.xlabel('Número')
    plt.ylabel('Tempo de execução (segundos)')
    plt.title('Comparação de Notação Big O')
    plt.legend()
    plt.show()

# Executar os testes
# compare_execution_time()
# compare_big_o_notation()