import random

def main():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Higher!")
            elif guess > number_to_guess:
                print("Lower!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()