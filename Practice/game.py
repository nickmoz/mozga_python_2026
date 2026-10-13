# Create a game where a user must keep entering a doors until they reach the exit.
# They have 3 doors, one is safe and two are traps.
# They have 2 lives to get through 3 doors.
import random
print("Welcome to the door game!")

round = 1
lives = 2


while lives > 0:
    print("Round", round)
    print("Lives:", lives)

    choice = (input("Would you like to enter Door A, B, or C?: "))
    event = ["TRAP", "SAFE"]
    r = random.randint(0, 1)
    outcome = event[r]
    print(outcome)

    if choice == 'A' or choice == 'B' or choice == 'C':

        if outcome == 'SAFE':
            round += 1
            print("This door is safe and you advance.")
            continue
        if round == 3:
            print("Congragulations, you found the exit")
            break
        if outcome == 'TRAP':
            lives -= 1
            round += 1
            print("This door is a trap and you have lost a life.")
            continue
        if lives == 0:
            print("You are out of lives.")
            break

print("GAME OVER")
