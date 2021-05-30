import random
from termcolor import colored
import colorama

colorama.init()
def getDifferentRandomNumbers(l, u, amount):
    nums = list(range(l, u + 1))
    out = []
    for i in range(amount):
        x = random.choice(nums)
        out.append(x)
        nums.remove(x)
    return out


execute = True

while True:

    if not execute:
        rand = "n"
    else:
        rand = input("Should I select your numbers randomly? (y or n): ")

    if rand.lower().startswith(
        "y"
    ):  # The user would like their numbers to be randomly selected.
        whiteBalls = getDifferentRandomNumbers(1, 69, 5)
        powerBall = random.randint(1, 26)

    else:  # Have the user input their numbers

        # Get the five white balls
        if execute:  # Skip this section if the Powerball is invalid
            while True:
                success = True
                try:
                    whiteBalls = [
                        int(x)
                        for x in input(
                            "Enter five DIFFERENT numbers from 1 to 69, separated by spaces (i.e. 1 34 65 43 7). These will be your five white balls. > "
                        ).split(" ")
                    ]
                except:
                    print("Sorry, but your numbers aren't valid. Please try again. ")
                    continue
                for i in whiteBalls:
                    if (
                        not (1 <= i <= 69)
                        or sorted(list(set(whiteBalls))) != sorted(whiteBalls)
                        or len(whiteBalls) != 5
                    ):
                        success = False
                        print(
                            "Sorry, but your numbers aren't valid. Please try again. "
                        )
                        break
                if not success:
                    continue
                break

        # Get the red Powerball
        try:
            powerBall = int(
            input("Now enter a number from 1 to 26. This is your Powerball. > ")
        )
        except:
            print("Sorry, but your Powerball is invalid. Please try again.")
            execute = False
            continue            
        if not 1 <= powerBall <= 26:
            print("Sorry, but your Powerball is invalid. Please try again.")
            execute = False
            continue

    drawingWhite = getDifferentRandomNumbers(1, 69, 5)
    drawingRed = random.randint(1, 26)

    correctWhiteBalls = len([b for b in whiteBalls if b in drawingWhite])
    powerBallMatch = powerBall == drawingRed

    print("\nThe red number is the Powerball.")
    print(
        f"Today's drawings are: \
        {' '.join([str(x) for x in drawingWhite])}",
        colored(str(drawingRed), "red"),
    )

    prizes = {
        (5, True): "Congratulations! You just won the grand prize! ($100,000,000)",
        (5, False): "You won $1,000,000!",
        (4, True): "You won $50,000!",
        (4, False): "You won $100.",
        (3, True): "You won $100.",
        (3, False): "You won $7.",
        (2, True): "You won $7.",
        (1, True): "You won $4.",
        (0, True): "You won $4",
    }

    print(
        f"Your drawings are:    \
        {' '.join([str(x) for x in whiteBalls])}",
        colored(str(powerBall), "red"),
    )

    if tuple([correctWhiteBalls, powerBallMatch]) not in prizes.keys():
        prize = "Sorry, you didn't win anything. Try again next time!"
    else:
        prize = prizes[tuple([correctWhiteBalls, powerBallMatch])]

    print(prize)

    playAgain = input("Would you like to play again? (y or n): ")
    if playAgain.lower().startswith("y"):
        execute = True
        continue
    else:
        break
