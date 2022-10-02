import numpy as np

number = np.random.randint(1,101)#pick number
count = 0

while True:
    count += 1
    predict_number = int(input("Guess number from 1 to 100:")) 
    
    if predict_number > number:
        print("Number must be lower!")
        
    elif predict_number < number:
        print("Number must be higher!")
        
    else:
        print(f"You have guessed the number! It is ={number}, it took you {count} guesses")
        break #game over, end cycle 
