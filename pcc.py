import random

max_combinations = int(input("\nHow many numbers would you like to enter?\n\n \
    \tPlease note that entering any number higher than 7 will result in \n \tcalculations times taking several minutes or more!\n\n \
    :"))

max_combination_counter = list(range(1, max_combinations+1))

numbers = []

for num in range(1, max_combinations+1):
    number = int(input("Please enter a unique number: "))
    if number not in numbers:
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

print(f"Possible combinations: {max_combinations[-1]}")

for value in possible_combinations.values():
    print(f"{(str(value)[1:-1])}")

