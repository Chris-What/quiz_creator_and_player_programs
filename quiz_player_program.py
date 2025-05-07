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
    print(Fore.RED + "Hmm... There's no quiz file, yet. Try using the Quiz Creator program first in order to use this one!")
    exit()

#3. display welcome message when opening the program
print(Fore.CYAN + Style.BRIGHT + "\nThink ya got the smarts? Then try this out! WELCOME to the QUIZ PLAYER!!")
print(Fore.YELLOW + "Answer questions made from the Quiz Creator program, and test your brain!")

#4. shuffle the questions, and start the quiz
random.shuffle(quiz_data)

score = 0
total = len(quiz_data)

for number, item in enumerate(quiz_data, start=1):
    print(Fore.MAGENTA + f'\nQuestion number {number}: {item["question"]}')
    for letter, choice in item["choices"].items():
        print(f"    {letter}) {choice}")

    user_answer = input(Fore.CYAN + "What'll it be? A, B, C, or D?: ").strip().upper()

    if user_answer == item["correct_answer"]:
        print(Fore.GREEN + "DING DING DING!!! We got a smarty-pants here!")
        score += 1
    else:
        correct = item["correct_answer"]
        print(Fore.RED + f'Not quite! The correct answer is {correct}: {item["choices"][correct]}')

#5. display the final score achieved
print(Fore.BLUE + "\nMade it to the end! Hardly broke a sweat? Or were tears running down your face? Let's find out if you aced this quiz!")
print(Fore.YELLOW + f"Drumroll please! *krrrr....*\nYour score is.... {score} out of {total}!")

percent = (score / total) * 100

if percent == 100:
    print(Fore.GREEN + Style.BRIGHT + "Are you Albert Einstein or something?? You're a GENIUS!!!")
elif percent >= 75:
    print(Fore.GREEN + "Ya got a bright future ahead of ya, kid. One day, you might be in the history books!")
elif percent >= 50:
    print(Fore.YELLOW + "Not bad! Keep working and you'll be better in no time!")
else:
    print(Fore.RED + "Oh... Don't worry, we all have those moments. Just keep trying and you'll get there!")

#6. display final message when done with the quiz
print(Fore.CYAN +Style.BRIGHT + "\nNo matter if your score is low or high, what matters is that we learn, and have fun while doing so! Thank you, dear user, for answering this quiz in the QUIZ PLAYER PROGRAM!!!")