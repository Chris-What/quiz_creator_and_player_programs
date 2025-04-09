#1. display message when opening the program
print("Welcome to Quiz Creator! This program allows you to create questions to be used in a quiz. To start, enter a question below.")

#2. initiate the name of the text file where the quiz questions will go to
filename = "quiz_questions.txt"

#3. overwrite any previous data written in the text files
with open(filename, "w") as file:
    pass

#4. initiate the start of the question numbers to be used in the text file for formatting
question_num = 1

#5. ask the user to enter a question, four choices to choose from, and the correct answer
while True:
    question = input("Enter a question for the quiz: ")
    choice_a = input("Enter choice A: ")
    choice_b = input("Enter choice B: ")
    choice_c = input("Enter choice C: ")
    choice_d = input("Enter choice D: ")

    correct_ans = ""
    while correct_ans not in ["A", "B", "C", "D"]:
        correct_ans = input("Which choice is the correct answer? (A/B/C/D): ").upper()

        if correct_ans not in ["A", "B", "C", "D"]:
            print("Invalid input; please choose between A, B, C, or D.")

#6. put the questions and choices in the text file

#7. ask the user if they want to enter another set of questions and choices

#8. display exit message when the user is done with the program