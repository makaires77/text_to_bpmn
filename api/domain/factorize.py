# paradigms/domain/factorize.py

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
