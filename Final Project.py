from time import sleep
import random
from random import randint
from random import shuffle

# Define functions for GuessTheRoll
def GameMenu():
    choice = 0
    while choice < 1 or choice > 3:
        try:
            print("1) See Rules\n2) Play Game\n3) Return to Main Menu\n")
            choice = int(input("Please choose from the menu: "))
            if choice < 1 or choice > 3:
                print("Please enter only 1, 2, or 3\n")
        except ValueError:
            print("\nMust type a number\n")
    return choice

def sideOne():
    print("___________")
    print("|           |")
    print("|           |")
    print("|     O     |")
    print("|           |")
    print("|___________|")

def sideTwo():
    print("___________")
    print("|           |")
    print("|  O        |")
    print("|           |")
    print("|        O  |")
    print("|___________|")

def sideThree():
    print("___________")
    print("|           |")
    print("|  O        |")
    print("|     O     |")
    print("|        O  |")
    print("|___________|")

def sideFour():
    print("___________")
    print("|           |")
    print("|  O     O  |")
    print("|           |")
    print("|  O     O  |")
    print("|___________|")

def sideFive():
    print("___________")
    print("|           |")
    print("|  O     O  |")
    print("|     O     |")
    print("|  O     O  |")
    print("|___________|")

def sideSix():
    print("___________")
    print("|           |")
    print("|  O     O  |")
    print("|  O     O  |")
    print("|  O     O  |")
    print("|___________|")

def diceDisplay():
    diceNum = random.randint(1, 6)
    if diceNum == 1:
        sideOne()
    elif diceNum == 2:
        sideTwo()
    elif diceNum == 3:
        sideThree()
    elif diceNum == 4:
        sideFour()
    elif diceNum == 5:
        sideFive()
    elif diceNum == 6:
        sideSix()
    return diceNum

def GuessTheRoll():
    ROUNDS = 5
    menuSelection = diceOne = diceTwo = diceTotal = playerGuess = score = compScore = 0
    while True:
        print("\n\nWelcome to my guess the dice sum game\n\n")
        sleep(1)
        print("GUESS\n")
        sleep(1)
        print("THE\n")
        sleep(1)
        print("SUM\n")
        sleep(1)
        menuSelection = GameMenu()
        if menuSelection == 1:
            print("\n" + "*" * 40)
            print("\nThe player tries to guess what the sum of the 2 dice thrown will be.")
            print("If the player guesses right they earn points. If not, the computer gets a point.")
            print("Highest score after 5 rounds wins.\n")
            print("*" * 40 + "\n")
        elif menuSelection == 2:
            score = compScore = 0
            for i in range(ROUNDS):
                playerGuess = 0
                print(f"\n{'*' * 40}")
                print(f"ROUND {i + 1}")
                print(f"{'*' * 40}")
                while playerGuess < 2 or playerGuess > 12:
                    try:
                        playerGuess = int(input("\nPlease guess a sum of the two dice (2-12): "))
                        if playerGuess < 2 or playerGuess > 12:
                            print("\nYour guess must be between 2 and 12. Please try again.")
                    except ValueError:
                        print("Please enter a number.")
                sleep(1)
                print("\nHere comes the first roll...")
                sleep(0.5)
                diceOne = diceDisplay()
                print("\nHere comes the second roll...")
                sleep(0.5)
                diceTwo = diceDisplay()
                diceTotal = diceOne + diceTwo
                print(f"\nThe roll totaled {diceTotal}")
                if playerGuess == diceTotal:
                    print(f"\n\nYour guess was {playerGuess} - An exact match! You get 1 point!")
                    score += 1
                else:
                    print(f"\n\nSorry, your guess of {playerGuess} is not correct")
                    compScore += 1
                print(f"\nCurrent score: \nPlayer: {score}\nComputer: {compScore}\n\n")
            if score > compScore:
                print(f"All {ROUNDS} rounds are finished. The winner is Player!")
            elif compScore > score:
                print(f"All {ROUNDS} rounds are finished. The winner is Computer!")
            else:
                print(f"All {ROUNDS} rounds are finished. It's a tie!")
        elif menuSelection == 3:
            print("\nReturning to Main Menu...\n")
            return # Exit the function to return to main menu

def HighCardWins(name):
    KING = """\
     ____ 
    |K   |
    |  ♣️ |
    |   K|
    ----  
    """
    QUEEN = """\
     ____ 
    |Q   |
    |  ♣️ |
    |   Q|
    ----  
    """
    JACK = """\
     ____ 
    |J   |
    |  ♣️ |
    |   J|
    ----  
    """
    TEN = """\
     ____ 
    |10  |
    |  ♣️ |
    |  10|
    ----  
    """
    NINE = """\
     ____ 
    |9   |
    |  ♣️ |
    |   9|
    ----  
    """
    EIGHT = """\
     ____ 
    |8   |
    |  ♣️ |
    |   8|
    ----  
    """
    SEVEN = """\
     ____ 
    |7   |
    |  ♣️ |
    |   7|
    ----  
    """
    SIX = """\
     ____ 
    |6   |
    |  ♣️ |
    |   6|
    ----  
    """
    FIVE = """\
     ____ 
    |5   |
    |  ♣️ |
    |   5|
    ----  
    """
    FOUR = """\
     ____ 
    |4   |
    |  ♣️ |
    |   4|
    ----  
    """
    THREE = """\
     ____ 
    |3   |
    |  ♣️ |
    |   3|
    ----  
    """
    TWO = """\
     ____ 
    |2   |
    |  ♣️ |
    |   2|
    ----  
    """
    ACE = """\
     ____ 
    |A   |
    |  ♣️ |
    |   A|
    ----  
    """
    cardList = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]
    playerCard = menuSelection = compCard = playerScore = compScore = turn = 0
    print("\n\nWelcome to High Card Wins!\n")
    print("      HIGH\n")
    sleep(1)
    print("      CARD\n")
    sleep(1)
    print("      WINS\n")
    while menuSelection != 3:
        playerScore = compScore = 0
        menuSelection = GameMenu()
        if menuSelection == 1:
            print(f"\n{'*' * 40}")
            print("\nThe player draws a card\nThen the computer draws a card\nHighest card wins")
            print(f"\n{'*' * 40}")
        elif menuSelection == 2:
            while playerScore != 5 and compScore != 5:
                turn += 1
                print(f" Round {turn}   ".center(40, '♣'))
                input(f"\nOkay {name}, Press enter to draw a card: ")
                playerCard = randint(2, 14)
                compCard = randint(2, 14)
                sleep(.5)
                print(f"\nPlayer card is \n {cardList[playerCard - 2]}")
                sleep(.5)
                print("\nNow it's the computer's turn...")
                print(f"\nComputer card is \n {cardList[compCard - 2]}")
                if playerCard > compCard:
                    playerScore += 1
                    print(f"\nThe winner of round {turn} is {name}\n")
                elif compCard > playerCard:
                    compScore += 1
                else:
                    print(f"\nThe winner of round {turn} is the computer\n")
                print(f"Running score after round {turn}: \n{name} = {playerScore} \nComputer = {compScore}\n")
            if playerScore > compScore:
                print(f"{name} wins after {turn} rounds")
            elif compScore > playerScore:
                print(f"Computer wins after {turn} rounds")
            else:
                print(f"The game ends in a tie after {turn} rounds")
        elif menuSelection == 3:
            print("\nReturning to Main Menu...\n")
            return  # Exit the function to return to the main menu


import random

# Define biology trivia questions and answers
insect_trivia_questions = [
    ("How long have cockroaches been around?", ["200 years", "500 years", "1000 years", "Since the dinosaurs"], "Since the dinosaurs"),
    ("Which pest gets its name from the large white patches on its face?", ["Carpet beetle", "Black widow spider", "Bald-faced hornet", "Blacklegged deer tick"], "Bald-faced hornet"),
    ("A rat can squeeze into your home through a hole the size of what?", ["Penny", "Nickel", "Dime", "Quarter"], "Quarter"),
    ("Which pest feeds on human blood?", ["Ant", "Bed Bug", "Stink Bug", "Wasp"], "Bed Bug"),
    ("What happens to an ant colony when the queen dies?", ["A new queen is crowned", "The colony divides into smaller colonies", "The colony disappears", "None of the above"], "The colony disappears")
]

def BiologyTrivia():
    # Define variables
    playerScore = 0
    menuSelection = 0

    while True:
        # Display Menu
        print("\n\nWelcome to the Insect Trivia Game!\n")
        print("1) See Rules")
        print("2) Play Game")
        print("3) Return to Main Menu")
        try:
            menuSelection = int(input("Please choose from the menu: "))
        except ValueError:
            print("Please enter a number.")
            continue
        
        if menuSelection == 1:
            print("\n" + "*" * 40)
            print("In this trivia game, you will be asked 5 questions about insects.")
            print("You will have to choose the correct answer from 4 options.")
            print("Correct answers will earn you points. Good luck!")
            print("*" * 40 + "\n")
        
        elif menuSelection == 2:
            # Shuffle questions to avoid repetition
            random.shuffle(insect_trivia_questions)
            
            # Ask 5 questions
            for q in range(5):
                question, options, correct_answer = insect_trivia_questions[q]
                print(f"\nQuestion {q + 1}: {question}")
                for i, option in enumerate(options):
                    print(f"{i + 1}) {option}")
                try:
                    answer = int(input("Choose the correct option (1-4): "))
                    if options[answer - 1] == correct_answer:
                        print("Correct!")
                        playerScore += 1
                    else:
                        print(f"Wrong! The correct answer was {correct_answer}.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue

            print(f"\nYour total score is: {playerScore}")
            break
        
        elif menuSelection == 3:
            print("\nReturning to Main Menu...\n")
            return
        
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


def MathGame():
    def generate_questions(difficulty):
        if difficulty == "Easy":
            num_questions = 5
            operations = ["+", "-"]
        elif difficulty == "Moderate":
            num_questions = 5
            operations = ["+", "-", "*"]
        elif difficulty == "Hard":
            num_questions = 5
            operations = ["+", "-", "*", "/"]
        questions = []
        for _ in range(num_questions):
            num1 = randint(1, 10) if difficulty == "Easy" else randint(1, 20)
            num2 = randint(1, 10) if difficulty != "Hard" else randint(1, 20)
            operation = random.choice(operations)
            if operation == "+":
                answer = num1 + num2
            elif operation == "-":
                answer = num1 - num2
            elif operation == "*":
                answer = num1 * num2
            elif operation == "/":
                num1 = num2 * randint(1, 10)  # To ensure integer division
                answer = num1 // num2
            question = f"What is {num1} {operation} {num2}?"
            questions.append((question, answer))
        return questions

    def ask_questions(difficulty):
        questions = generate_questions(difficulty)
        score = 0
        for question, answer in questions:
            try:
                user_answer = int(input(f"\n{question} "))
                if user_answer == answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer was {answer}.")
            except ValueError:
                print("Please enter a valid number.")
        print(f"\nYour final score for {difficulty} difficulty is {score} out of {len(questions)}.")

    while True:
        difficulty = input("\nSelect difficulty level (Easy, Moderate, Hard): ").capitalize()
        if difficulty in ["Easy", "Moderate", "Hard"]:
            ask_questions(difficulty)
            break
        else:
            print("Invalid difficulty level. Please choose from Easy, Moderate, or Hard.")

def main():
    name = input("What is your name? ")
    while True:
        print("\nMain Menu")
        print("1) GuessTheRoll")
        print("2) HighCardWins")
        print("3) TriviaGame")
        print("4) MathGame")
        print("5) Quit")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                GuessTheRoll()
            elif choice == 2:
                HighCardWins(name)
            elif choice == 3:
                BiologyTrivia()
            elif choice == 4:
                MathGame()
            elif choice == 5:
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
