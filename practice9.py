import random

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user
# to guess the number, then tell them whether they guessed too low, too high,
# or exactly right.

random_num = random.randint(1,9)
attempts = 0
player_score = 0

print("Welcome to random number guesser!\nIf you guess the number correctly, you get a point.\nIf you don't guess right you can try again.\nOnce you guess the number right, a new number will be generated.")

while True:
    # tester on the line below
    # print(random_num)

    exit_choice = input("type '1' to play or type '2' to quit: ")
    if exit_choice == '2':
        break
    user_guess = int(input("Select a number between 1-9: "))

    if user_guess == random_num:
        player_score += 1
        print("YOU GUESSED RIGHT!!")
        random_num = random.randint(1,9)
    elif user_guess > random_num:
        print("Too high...")
    elif user_guess < random_num:
        print("Too low...")
    else:
        print("You didn't guess a number between 1-9...")

    attempts += 1

print("You guessed right {0} times out of {1} attempts!".format(player_score, guesses))
print("Thanks for playing!")
