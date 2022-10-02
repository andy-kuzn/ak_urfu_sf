"""Guess the Number Game
Computer picks a number and guesses it by itself
"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess a number

    Args:
        number (int, optional): Picked number. Defaults to 1.

    Returns:
        int: Nunber of guesses
    """

    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # guessed number
        if number == predict_number:
            break # end cycle if correct number is guessed
    return(count)

#print(f'Number of guesses:{random_predict()}')

def score_game(random_predict) -> int:
    """How many guesses on average it takes the algorythm to guess 
    the number after 100 runs 

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of guesses
    """
    
    count_ls = [] # list for storing numbers of guesses
    np.random.seed(1) # fix 'seed' for repeatability
    random_array = np.random.randint(1, 101, size=(1000)) #list of picked numbers
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
        
    score = int(np.mean(count_ls)) #calculate average number of guesses
    
    print(f'Your algorythm gives the correct number in {score} guesses on average')
    return(score)

# RUN
score_game(random_predict)