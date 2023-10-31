import random

print("Welcome to the Fishing Game!")
print("Try to catch the big fish!")

fish_size = random.randint(1, 10)  # Random fish size between 1 and 10

while True:
    try:
        player_guess = int(input("Enter your guess (between 1 and 10): "))
        if 1 <= player_guess <= 10:
            break
        else:
            print("Invalid guess. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if player_guess == fish_size:
    print(f"Congratulations! You caught the fish! Its size: {fish_size}")
else:
    print(f"Sorry, you missed! The fish size was: {fish_size}")
