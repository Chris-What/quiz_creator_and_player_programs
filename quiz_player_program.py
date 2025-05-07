import json
import random
from colorama import init, Fore, Style

#1. initialize colorama
init(autoreset=True)

#2. load the json file containing the quiz questions
filename = "quiz_questions.json"

try:
    with open(filename, "r") as file:
        quiz_data = json.load(file)
except FileNotFoundError:
    print("Hmm... There's no quiz file, yet. Try using the Quiz Creator program first in order to use this one!")
    exit()

#3. display welcome message when opening the program
print("\nThink ya got the smarts? Then try this out! WELCOME to the QUIZ PLAYER!!")
print("Answer questions made from the Quiz Creator program, and test your brain!")

#4. shuffle the questions, and start the quiz
random.shuffle(quiz_data)

score = 0
total = len(quiz_data)

for number, item in enumerate(quiz_data, start=1):
    print(f'\nQuestion number {number}: {item["question"]}')
    for letter, choice in item["choices"].items():
        print(f"{letter}){choice}")

    user_answer = input("What'll it be? A, B, C, or D?: ").strip().upper

    if user_answer == item["correct_answer"]:
        print("DING DING DING!!! We got a smarty-pants here!")
        score += 1
    else:
        
#5. display the final score achieved

#6. display final message when done with the quiz