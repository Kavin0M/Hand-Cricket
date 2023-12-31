from random import randint
def bot():
    a = randint(1,9)
    return a

def wincon(a,b):
    if a==b:
        return False
    else:
        return True
    
def choice(a,b):
    if (a+b)%2==0:
        return "even"
    else:
        return "odd"

def check(a):
    if a  not in ['1','2','3','4','5','6','7','8','9']:
        return True
    else:
        return False
    
while True:
    n = input("\nEnter odd or even: ")
    while n not in ["odd","even","Odd","Even"]:
        print("\nInvalid input !! Enter a valid one")
        n = input("Enter odd or even: ")
    n = n.lower()

    a = input("\nEnter a number between 1 and 9: ")
    while check(a):
        print("\nInvalid input !! Enter a valid input")
        a = input("Enter a number between 1 and 9: ")
    a = int(a)
    b = bot()

    outcome = choice(a,b)
    p,b = 0,0
    if outcome == n:
        print("\nPlayer's turn to choose")
        p = input("Choose batting or bowling (1 or 2): ")
        while p not in ['1','2']:
            print("\nInvalid input !! Enter a valid one")
            p = input("Choose batting or bowling (1 or 2): ")
    else:
        print("Bot's turn to choose")
        b = randint(1,2)

    if p == "1" or b == "2":
        player = "batter"
        robot = "bowler"
    else:
        player = "bowler"
        robot = "batter"
    print(f"\nPlayer 1 is the {player}\nBot is the {robot}")

    score1 = 0
    score2 = 0
    if player == "batter":
        b = bot()
        r = 0
        while wincon(int(r),b):
            r = input("Enter a number between 1 to 9: ")
            while check(r):
                print("\nInvalid input !! Enter a valid input")
                r = input("Enter a number between 1 to 9: ")
            b = bot()
            print(f"Bot's number: {b}")
            score1 += int(r)
            print(f"\n\tScore of player1: {score1}")
        else:
            print("\n\tPlayer1 is out")

    else:
        b = bot()
        r = 0
        while wincon(int(r),b):
            r = input("Enter a number between 1 to 9: ")
            while check(r):
                print("\nInvalid input !! Enter a valid input")
                r = input("Enter a number between 1 to 9: ")
            b = bot()
            print(f"Bot's number: {b}")
            score2 += b
            print(f"\n\tScore of Bot: {score2}")
        else:
            print("\n\tBot is out")

    player, robot = robot, player
    print(f"\nPlayer 1 is the {player}\nBot is the {robot}")
    
    game = True
    if player == "bowler":
        while (game):
            b = bot()
            r = 0
            while wincon(int(r),b):
                r = input("Enter a number between 1 to 9: ")
                while check(r):
                    print("\nInvalid input !! Enter a valid input")
                    r = input("Enter a number between 1 to 9: ")
                b = bot()
                print(f"Bot's number: {b}")
                score2 += b
                print(f"\n\tScore of Bot: {score2}")
                if score1<score2:
                    print("\n\tBot wins")
                    game = False
            else:
                print("\n\tBot is out")
                print("\n\tPlayer1 wins")
                break

    else:
        while (game):
            b = bot()
            r = 0
            while wincon(int(r),b):
                r = input("Enter a number between 1 to 9: ")
                while check(r):
                    print("\nInvalid input !! Enter a valid input")
                    r = input("Enter a number between 1 to 9: ")
                b = bot()
                print(f"Bot's number: {b}")
                score1 += int(r)
                print(f"\n\tScore of player1: {score1}")
                if score1 > score2:
                    print("\n\tPlayer1 wins")
                    game = False
            else:
                print("\n\tPlayer1 is out")
                print("\n\tBot wins")
                break

    again = input("\nDo you want to play again ? (y or n)")
    while again not in ["y","n","Y","N"]:
        print("\nInvalid input !! Enter a valid input")
        again = input("\nDo you want to play again ? (y or n): ")
    if again in ["n","N"]:
        break