import random

def random_number(a, b):
    return random.randint(min(a,b), max(a, b))

number = []
for i in range(random_number(2, 20)):
    number.append(random_number(0, 100))

print(number)

first_biggest = max(number)

number.remove(first_biggest)

second_biggest = max(number)

print(f"The two biggest numbers are {first_biggest} and {second_biggest}")