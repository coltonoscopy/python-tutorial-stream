'''
CS50 Python Tutorial

Number game with a heart display.
'''

import random

FULL_HEALTH = 3
FULL_HEART = '♥'
EMPTY_HEART = '♡'

def print_life(life):
    for i in range(life):
        print(FULL_HEART, end='')
    
    for i in range(FULL_HEALTH - life):
        print(EMPTY_HEART, end='')
    
    print()

if __name__ == '__main__':
    
    # one point for each heart
    life = FULL_HEALTH

    score = 0

    while life > 0:

        # grab two random numbers to add or subtract
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)

        # randomly add or subtract numbers, storing operator
        if random.randint(0, 1) == 1:
            sign = '+'
            solution = num1 + num2
        else:
            sign = '-'
            solution = num1 - num2
        
        # print hearts and prompt for input
        print_life(life)
        print(f'Your Score: {score}\n')
        answer = int(input(f'{num1} {sign} {num2}: '))

        # test answer and damage health if needed
        if sign == '+':
            if answer == num1 + num2:
                score += 1
                print(f'Correct! {num1} {sign} {num2} = {answer}!')
            else:
                life -= 1
                print(f'Wrong! {num1} {sign} {num2} = {num1 + num2}, not {answer}!')
        else:
            if answer == num1 - num2:
                score += 1
                print(f'Correct! {num1} {sign} {num2} = {answer}!')
            else:
                life -= 1
                print(f'Wrong! {num1} {sign} {num2} = {num1 - num2}, not {answer}!')
        print()

    print_life(life)
    print(f'Tragically, your journey has come to an end.')
    print(f'You reached a score of {score}!')
