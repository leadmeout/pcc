import random

max_combinations = int(input("How many numbers would you like to enter?\n"))
max_combination_counter = list(range(1, max_combinations+1))

numbers = []

for num in range(1, max_combinations+1):
    number = int(input("Please enter a unique number: "))
    numbers.append(number)
    
max_combinations = 1

for num in max_combination_counter:
    max_combinations *= num

max_combinations = list(range(1, max_combinations+1))

possible_combinations = {}
possible_combinations[1] = numbers
count = 2

while count != max_combinations[-1]:

    new_combination = random.sample(numbers, len(numbers))

    if new_combination not in possible_combinations.values():
        possible_combinations[count] = new_combination
        count += 1
    else:
        continue

for value in possible_combinations.values():
    print(f"{value}")

