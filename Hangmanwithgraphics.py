#Hangman Updated

import random
from graphics import *

def choose_word_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_" " " " "
    return displayed_word

def draw_hangman(win, wrong_guesses):
    if wrong_guesses == 1:
        head = Circle(Point(450, 225), 40)
        head.draw(win)
    elif wrong_guesses == 2:
        body = Line(Point(450, 265), Point(450, 450))
        body.draw(win)
    elif wrong_guesses == 3:
        leftarm = Line(Point(450, 275), Point(400, 325))
        leftarm.draw(win)
    elif wrong_guesses == 4:
        rightarm = Line(Point(450, 275), Point(500, 325))
        rightarm.draw(win)
    elif wrong_guesses == 5:
        leftleg = Line(Point(450, 450), Point(400, 500))
        leftleg.draw(win)
    elif wrong_guesses == 6:
        rightleg = Line(Point(450, 450), Point(500, 500))
        rightleg.draw(win)

def hangman(file_path):
    word = choose_word_from_file(file_path)
    guessed_letters = []
    attempts = 6
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")

    win = GraphWin("Hangman", 700, 700)
    
    line1 = Line(Point(200, 125), Point(200, 550))
    line1.draw(win)
    line2 = Line(Point(200, 125), Point(450, 125))
    line2.draw(win)
    rope = Line(Point(450, 125), Point(450, 185))
    rope.draw(win)
    bar = Polygon(Point(200, 185), Point(200, 125), Point(283.3, 125))
    bar.draw(win)

    print(display_word(word, guessed_letters))

    while attempts > 0 and "_" in display_word(word, guessed_letters):
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            wrong_guesses += 1
            draw_hangman(win, wrong_guesses)
            print("Incorrect! You have", attempts, "attempts left.")
        print(display_word(word, guessed_letters))


    if "_" not in display_word(word, guessed_letters):
        print("Congratulations, you guessed the word!")
    else:
        print("Out of attempts! The word was:", word)

        win.getMouse()
        win.close()

hangman('words.txt')

