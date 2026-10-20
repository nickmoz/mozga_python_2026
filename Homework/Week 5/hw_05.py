# Rebuild the Hangman game as a class. The class will include a method for each task.
import random
import requests


class Hangman:

    def __init__(self):
        self.secret = self.random_word()
        self.wrong = []
        self.correct = []
        self.display = self.create_display_from_secret()

    def random_word(self):
        response = requests.get("https://random-word-api.herokuapp.com/word")
        data = response.json()
        word = data[0]
        return word

    def create_display_from_secret(self):
        display = self.secret[0]

        for i in range(1, len(self.secret) - 1):
            if self.secret[i] in self.correct:
                display += self.secret[i]
            else:
                display += "_"

        display += self.secret[-1]
        return display

    def guess_letter(self):
        guess = input("Guess a letter: ")

        if len(guess) > 1:
            print("Enter one letter only.")
            return

        guess = guess.lower()

        if guess in self.secret:
            if guess not in self.correct:
                self.correct.append(guess)
        else:
            if guess not in self.wrong:
                self.wrong.append(guess)

        self.display = self.create_display_from_secret()

    def check_winner(self):
        if self.display == self.secret:
            print("Found")
            return True

        if len(self.wrong) == 6:
            print("You are hanged")
            return True
        return False

    def play(self):
        while True:
            print(self.display)
            self.guess_letter()

            if self.check_winner():
                break

        print("GAME OVER")


game = Hangman()
game.play()

# AI Disclaimer: This code was generated with the help of AI.

# Make the load random word method retrieve a word from an API: https://random-word-api.herokuapp.com/word
