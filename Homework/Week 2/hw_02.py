# Write a function to convert Celsius temperature to Fahrenheit and the opposite.
# F = (C * 9/5) + 32
# C = (F - 32)/1.8

import random
unit = input('What unit? (C/F): ')

if unit == 'C':
    temp = float(input('Enter Temperature in C: '))
    fahrenheit = (temp * 9/5) + 32
    print(f'{fahrenheit}')

elif unit == 'F':
    temp = float(input('Enter Temperature in F: '))
    celsius = (temp - 32) / 1.8
    print(f'{celsius}')

else:
    print('Error')

# **********************************************************************************#

# Write a function to calculate and return the factorial, n!, of a number n.
# 0! = 1
# 1! = 1

n = int(input("Enter a number: "))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))

# **********************************************************************************#

numbers1 = []

for i in range(20):
    numbers1.append(random.randint(1, 100))

print(numbers1)

even_count = 0

for number in numbers1:
    if number % 2 == 0:
        print('Even: ', number)
        even_count += 1

print('Total Even Numbers: ', even_count)


numbers2 = []

for i in range(20):
    numbers2.append(random.randint(1, 100))

print(numbers2)

for number in numbers2:
    if number in numbers1:
        print('Same: ', number)

# **********************************************************************************#


sales = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
]

for row in sales:
    year = row[0]
    total = sum(row[1:])
    print(year, '=', total)

for row in sales:
    year = row[0]
    total = sum(row[1:])
    mean = total / 4
    print(year, '=', mean)
