import random
from art import logo

print(logo)

def check(guess, number, life):
    '''For a random number chosen by the system, the user provides the guess against it. If it's right the user wins, otherwise the user loses a life.'''
    if guess == number:
        print(f"You've got the right answer: {number}")

    elif guess > number:
        print("Your guess is higher. Choose a lower value.")
        return life - 1

    elif guess < number:
        print("Your guess is lower. Choose a higher value.")
        return life - 1


def game():
    '''The game is about guessing the number in least tries as possible. The hard difficulty is choosing the number in 5 tries and easier version is choosing the number in 10 tries.'''

    print("Welcome to the number guessing game. I'm thinking of a number between 1 and 100. Try to guess it ;)")
    mode = input("Choose your mode of difficulty: 'Easy' or 'Hard' \n").lower()
    if mode == "easy":
        lives = 10
    else:
        lives = 5
    
    num = random.randint(1, 100)
    guess_num = 0
    while guess_num != num:
        print(f"You've {lives} remaining to guess the right number.")
        guess_num = int(input("Enter a number between 1 and 100: "))
        lives = check(guess_num, num, lives)

        if lives == 0:
            print(f"You've ran out of lives. The right answer was {num}")
            return
            
game()