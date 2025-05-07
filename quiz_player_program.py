import json
import random
from colorama import init, Fore, Style

#1. initialize colorama
init(autoreset=True)

#2. load the json file containing the quiz questions
filename = "quiz_questions.json"

try:
    with open(filename, "r") as file:
        quiz_date = json.load(file)
except FileNotFoundError:
    print("Hmm... There's no quiz file, yet. Try using the Quiz Creator program first in order to use this one!")
    exit()

#3. display welcome message when opening the program

#4. shuffle the questions, and start the quiz

#5. display the final score achieved

#6. display final message when done with the quiz