# Write a function which count number of lines and number of words in a text.
# The text should be retrieved from a file. (Hint 1: read all lines and count them.
# Hint 2: For each line split with the white space as delimiter and count parts).

import random
file = open("data.txt")

line_count = 0
word_count = 0

for lines in file:
    line_count = line_count + 1
    word_count = word_count + len(lines.split())

print(line_count)
print(word_count)

# *********************************************************************************************

# You are asked to help a Car Rental company keep track of their vehicles.
# For each vehicle they need: plate number, total number of km
# The application will present the following menu:
# 1. Add Vehicle
# 2. View Vehicles
# 0. Exit

while True:
    print('Menu:\n', '1. Add Vehichle\n', '2. View Vehicle\n', '0. Exit\n')
    option = input('Enter your option: ')

    if option == '1':
        file = open('vehicles.txt', 'r')
        existing = file.read()

        plate = input('Enter the plate number: ')
        total = input('Enter the total KM: ')

        if f'Plate Number: {plate}, ' in existing:
            print('Error. This plate number already exists and cannot be added again.')
        else:
            file = open('vehicles.txt', 'a')
            file.write(f'Plate Number: {plate}, ')
            file.write(f'Total KM: {total}\n')
            print('Vehicle successfully added.')

    elif option == '2':
        file = open('vehicles.txt', 'r')
        vehicles = file.read()
        print(vehicles)

    elif option == '0':
        confirm = input('Are you sure you want to exit? (Yes/No): ')

        if confirm == 'Yes':
            print('Goodbye')
            break
        elif confirm == 'No':
            continue

    else:
        print('Invalid Option')
