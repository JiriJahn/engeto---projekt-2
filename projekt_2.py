"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie
author: Jiri Jahn
email: jiri.jahn@email.cz
discord: jirkaj. 
"""

import random
import time

#Definice uvodniho textu#

def welcome_message():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

#Definice parametru hry#

def generate_secret_number():
    digits = list(range(10))  # List čísel od 0 do 9
    random.shuffle(digits)
    
    # Zkontrolujeme, zda první číslice není nula, pokud ano, prohodíme ji s jinou náhodnou číslicí
    if digits[0] == 0:
        index = random.randint(1, 9)
        digits[0], digits[index] = digits[index], digits[0]
    
    # Vytvoříme čtyřmístné číslo z prvních čtyř číslic v seznamu
    secret_number = ''.join(map(str, digits[:4]))
    
    return int(secret_number)

def validate_guess(guess):
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) < 4 or guess[0] == '0':
        return False
    return True

def evaluate_guess(secret_number, guess):
    bulls = sum(1 for i in range(4) if str(secret_number)[i] == guess[i])
    cows = sum(1 for digit in str(secret_number) if digit in guess) - bulls
    return bulls, cows

def main():
    welcome_message()
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")

        if not validate_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique non-zero digits.")
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Correct! You've guessed the right number {secret_number} in {attempts} guesses!")
            print(f"That's {'amazing!' if attempts <= 5 else 'very good!' if attempts <= 10 else 'good!' if attempts <= 15 else 'not bad!' if attempts <= 20 else 'not so good!'}")
            print(f"Time taken: {elapsed_time:.2f} seconds")
            break
        
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

if __name__ == "__main__":
    main()
