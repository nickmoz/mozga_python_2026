# Task 1
print('Please enter your date of birth.')

day = input('What day?')
month = input('What month?')
year = input('What year?')

print(day + '/' + month + '/' + year)


# Task 2
# Ask user to give the year's income and calculate and print the tax.
# If income is less than 10000, tax is 8%, if between 10001 and 26000 tax is 12%, otherwise tax is 24%.
print('Enter your income')

income = float(input('Income: '))

if income <= 10000:
    tax = income * 0.08
elif 10001 <= income <= 26000:
    tax = income * 0.12
else:
    tax = income * 0.24

print('Tax:', tax)


# Task 3
# Write a program to ask 2 numbers, a and b, from the user. Then print all the numbers from a to b. Error if a >= b.
print('Choose a number for a and b. a must be less than b.')

a = int(input('a: '))
b = int(input('b: '))

if a < b:
    for number in range(a, b+1):
        print(number, end='')
else:
    print('Error')


# Task 4
# Write a program that prints all the even numbers from 2 to a number given by the user.
print('Give a number from 2 to 50')
number4 = int(input('Number: '))

for number4 in range(2, number4 + 1, 2):
    print(number4, end='')


# Task 5
# Write a program to calculate the total cost of a super market self-checkout.
print('Total Price')
total = 0

while True:
    price = float(input('Item Price: '))
    total = total + price
    more = input('Have more items? (y/n): ')

    if more == 'n':
        break

print('Total: ', total)
