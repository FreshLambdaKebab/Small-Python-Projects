import random

def roll(sides = 6):
    num_rolled = random.randint(1,sides)
    return num_rolled

def loop(sides = 6,high_score = 0):
    rolling = True
    points = 0

    restart = input("Menu:press Enter to play again, ""press q to QUIT")
    #if 'q' is pressed, exit the program
    if restart.lower() == "q":
        return

    num_rolled = roll()

    while rolling:

        print("number rolled: ",num_rolled)

        prev_num_rolled = num_rolled

        decision = input("hi or lo?")
        #roll again for the guess
        num_rolled = roll()
        print("dice rolls a ",num_rolled)
        if decision.lower() == "hi":
            if num_rolled > prev_num_rolled:
                print("nice! +1 point")
                points += 1
            elif num_rolled == prev_num_rolled:
                print("try again")
            else:
                print("you suck! you rolled a ",num_rolled)
                int(points)
                print("Points: ", points)
                rolling = False
                loop()
        elif decision.lower() == "lo":
            if num_rolled < prev_num_rolled:
               print("nice! +1 point",num_rolled)
               points += 1
            elif num_rolled == prev_num_rolled:
               print("try again")
            else:
               print("you lose! you rolled a", num_rolled)
               int(points)
               print("Points:", points)
               rolling = False
               loop()


    return prev_num_rolled

def main():
    sides = 6

    loop(sides)

    print("thanks for playing!")

main()