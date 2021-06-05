import random

def create_list_of_numbers(n):
    """Create list of random numbers up to n"""
    numbers = []
    for i in range(0, n):
        numbers.append(random.randint(1, 10*n))
    return numbers

print(create_list_of_numbers(5))
print(create_list_of_numbers(10))