"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    number = 2

    while len(list) != number_of_primes:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            list.append(number)

        number += 1

    return list
