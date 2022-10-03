# Project 0. Guess the Number

## Table of Contents
[1. Introduction](#introduction)  
[2. General Info](#general-info)  
[3. Contest Rules](#contest-rules)  
[4. Code Metrics](#code-metrics)   
[5. Algorythm](#algorythm)  
[6. Acknowledgments](#acknowledgments)  
[7. Project Outcome](#project-outcome)


### Introduction
The aim of this project is to guess the number 'picked' by the computer in the least possible number of tries.

:arrow_up:[Back to Contents](#table-of-contents)

### General Info
A python program needs to be written that would guess a randomly generated number in as few iterations as possible.

### Contest Rules
- The computer picks a random number from 0 to 100 and we need to guess it. To 'guess' means to write a program that is able to guess the number.
- The algorythm takes into account whether our guess is higher or lower than the picked number.

### Code Metrics
Results are judged based on the average number of tries needed to guess the picked number after 1000 runs of the algorythm.

### Algorythm
The basic approach is to split the original number sequence (from 1 to 100) roughly in half on each iteration of the cycle by comparing the number 'picked' by the computer with the rounded mean of the sequence. For rounding reasons, the borders of the seqence on the first iteration are set at 0 and 100 and the first 'guess' is 50 ((0+100) / 2). If the 'picked' number is higher than the rounded mean, the 'guess' becomes the floor for the new seqence, so the second 'guess' would be 75 ((50+100) /2). Likewise, if the 'picked' number is lower than the rounded mean, the 'guess' on the second iteration would be 25 ((0+50) / 2). The cycle is stopped when the 'guess' becomes equal to the 'picked' number, and the number of tries (iterations) that were needed to achive this result is recorded. After 1000 runs, the average number of tries is returned.     

### Acknowledgments
Part of the code in game_v3.py file (the score_game function) was provided by UrFU/Skillactory). It was used for this project with minor adaptations.

### Project Outcome
Learning to write high-quality code in Python is the main purpose of this project.

:arrow_up:[Back to Contents](#table-of-contents)