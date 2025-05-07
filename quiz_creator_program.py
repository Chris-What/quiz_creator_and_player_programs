import json

#1. display message when opening the program
print("Welcome to Quiz Creator! This program allows you to create questions to be used in a quiz. To start, enter a question below.")

#2. initiate an empty where the questions will be stored, as well as initiate its name
filename = "quiz_questions.json"

quiz_data = []

#3. ask the user to enter a question, four choices to choose from, and the correct answer
while True:
    question = input("Enter a question for the quiz: ")

    choices = {}
    choices["A"] = input("Enter choice A: ")
    choices["B"] = input("Enter choice B: ")
    choices["C"] = input("Enter choice C: ")
    choices["D"] = input("Enter choice D: ")

    correct_ans = ""
    while correct_ans not in ["A", "B", "C", "D"]:
        correct_ans = input("Which choice is the correct answer? (A/B/C/D): ").upper()

        if correct_ans not in ["A", "B", "C", "D"]:
            print("Invalid choice; please choose between A, B, C, or D.")

#4. Add the questions as a dictionary
    item = {
        "question": question,
        "choices": choices,
        "correct_answer": correct_ans
}

    quiz_data.append(item)

#5. ask the user if they want to enter another set of questions and choices
    while True:
        next_move = input("Do you want to enter another quiz question? (yes/no): ")
        if next_move.lower() == "yes":
            break
        elif next_move.lower() == "no":
            break
        else:
            print('Invalid choice; please choose between "yes" or "no".')
            continue
    if next_move.lower() == "no":
        break

#6. save the data to the json file
with open(filename, "w") as file:
    json.dump(quiz_data, file, indent=4)

#8. display exit message when the user is done with the program
print(f"Thank you for using the Quiz Creator! All quiz questions, choices, and correct answers have been saved to {filename}!")