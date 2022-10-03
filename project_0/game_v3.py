"""Guess the Number Game
Computer 'picks' a number and guesses it.
"""

from itertools import count
import numpy as np


def guess_number(number:int=1) -> int:
    """Guess the number randomly picked by computer

    Args:
        number (int, optional): picked number, defaults to 1

    Returns:
        int: number of tries it takes to guess the number
    """

    count = 0
    a = 0
    b = 100
    while True:
        count += 1
        guessed_number = round((a+b)/2) # Guess is in the middle of sequence.
        if number == guessed_number:
            break # End cycle if correct number is guessed.
        elif number > guessed_number:
            a = guessed_number # Guess becomes the floor for new sequence.
        elif number < guessed_number:
            b = guessed_number # guess becomes the ceiling for new sequence.
    return(count)


def score_game(guess_number) -> float:
    """How many guesses it takes the algorythm to guess the number on
    average after 1000 runs

    Args:
        guess_number ([type]): guessing function

    Returns:
        float: average number of guesses
    """
    
    count_ls = [] # list for storing number of tries on each run
    np.random.seed(1) # fix 'seed' for repeatability
    random_array = np.random.randint(1, 101, size=(1000)) 
    # list of randomly picked numbers
    
    for number in random_array:
        count_ls.append(guess_number(number))
        
    score = np.mean(count_ls) #calculate average number of guesses
    
    print(f'Algorythm guesses the correct number in {score} tries on average')
    return(score)


# RUN
score_game(guess_number)