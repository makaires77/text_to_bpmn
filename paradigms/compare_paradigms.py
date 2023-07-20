import timeit
import matplotlib.pyplot as plt
import numpy as np

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
    plt.ylabel('Tempo de execução (milissegundos)')
    plt.title('Comparação de Tempo de Execução')

    for i, value in enumerate(values):
        plt.text(i, value, f'{value*1000:.2f}', ha='center', va='bottom')

    plt.show()

def compare_big_o_notation():
    numbers = list(range(2, 21))
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

    # Aproximação da curva para cada algoritmo
    plt.plot(numbers, np.array(numbers)**2, label='Quadrático')
    plt.plot(numbers, np.log2(numbers), label='Logarítmico')
    plt.plot(numbers, numbers, label='Linear')

    plt.legend()
    plt.show()

# Resto do código...

# compare_execution_time()
# compare_big_o_notation()


# Executar os testes
# compare_execution_time()
# compare_big_o_notation()