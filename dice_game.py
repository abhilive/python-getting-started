import random

def roll_dice():
    return random.randint(1,6) + random.randint(1,6)

def main():
    player1 = input("Enter player 1's name:\n")
    player2 = input("Enter player 2's name:\n")

    roll1 = roll_dice();
    roll2 = roll_dice();

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, "Wins!")
    elif roll1 < roll2:
        print(player2, "Wins!")
    else:
        print("You Tie!")

main()