import random

class Dice:
    sides = 6
    num_rolled = random.randint(1,sides)
    high_score = 0#initially the high score is zero

    def roll(self):
        num_rolled = random.randint(1,self.sides)
        return num_rolled

    def loop(self):
        rolling = True
        points = 0

        restart = input("Menu:press Enter to play again, ""press q to QUIT")
        # if 'q' is pressed, exit the program
        if restart.lower() == "q":
            return

        num_rolled = self.roll()

        while rolling:

            print("number rolled: ", num_rolled)

            prev_num_rolled = num_rolled

            decision = input("hi or lo?")
            # roll again for the guess
            num_rolled = self.roll()
            print("dice rolls a ", num_rolled)
            if decision.lower() == "hi":
                if num_rolled > prev_num_rolled:
                    print("nice! +1 point")
                    points += 1
                elif num_rolled == prev_num_rolled:
                    print("try again")
                else:
                    print("you suck! you rolled a ", num_rolled)
                    int(points)
                    print("Points: ", points)
                    if points > self.high_score:
                        self.high_score = points
                    print("high score: ", self.high_score)
                    rolling = False
                    self.loop()
            elif decision.lower() == "lo":
                if num_rolled < prev_num_rolled:
                    print("nice! +1 point", num_rolled)
                    points += 1
                elif num_rolled == prev_num_rolled:
                    print("try again")
                else:
                    print("you lose! you rolled a", num_rolled)
                    int(points)
                    print("Points:", points)
                    if points > self.high_score:
                        self.high_score = points
                    print("high score: ", self.high_score)
                    rolling = False
                    self.loop()


        return prev_num_rolled
