# Make a two-player Rock-Paper-Scissors game.


player_one_score = 0
player_two_score = 0


while True:

    print("** ROCK PAPER SCISSORS **")
    print("Type 'q' at any time to quit.")

    choice1 = input("PLAYER 1 -- Choose: ").lower()
    if choice1 == 'q':
        break
    choice2 = input("PLAYER 2 -- Choose: ").lower()
    if choice2 == 'q':
        break


    if choice1 == 'paper':
        if choice2 == 'rock':
            player_one_score += 1
            print('Player 1 wins!')
        elif choice2 == 'scissors':
            player_two_score += 1
            print('Player 2 wins!')
        elif choice2 == 'paper':
            print("It's a tie!")
        else:
            print("Player 2 didn't choose rock, paper, or scissors...")

    elif choice1 == 'rock':
        if choice2 == 'scissors':
            player_one_score += 1
            print('Player 1 wins!')
        elif choice2 == 'paper':
            player_two_score += 1
            print('Player 2 wins!')
        elif choice2 == 'rock':
            print("It's a tie!")
        else:
            print("Player 2 didn't choose rock, paper, or scissors...")

    elif choice1 == 'scissors':
        if choice2 == 'paper':
            player_one_score += 1
            print('Player 1 wins!')
        elif choice2 == 'rock':
            player_two_score += 1
            print('Player 2 wins!')
        elif choice2 == 'scissors':
            print("It's a tie!")
        else:
            print("Player 2 didn't choose rock, paper, or scissors...")

    else:
        print("Player 1 didn't choose rock, paper, or scissors...")

if player_one_score > player_two_score:
    print("\n** PLAYER 1 WINS! **")
elif player_two_score > player_one_score:
    print("\n** PLAYER 2 WINS! **")
else:
    print("\n** IT'S A TIE! **")

print("\nFinal score\nPlayer 1: {0}\nPlayer 2: {1}".format(player_one_score, player_two_score))

print("\nThanks for playing!")
