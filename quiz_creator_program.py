#1. display message when opening the program
print("Welcome to Quiz Creator! This program allows you to create questions to be used in a quiz. To start, enter a question below.")

#2. initiate the name of the text file where the quiz questions will go to
filename = "quiz_questions.txt"

#3. overwrite any previous data written in the text files
with open(filename, "w") as file:
    pass

#4. initiate the start of the question numbers to be used in the text file for formatting

#5. ask the user to enter a question, four choices to choose from, and the correct answer

#6. put the questions and choices in the text file

#7. ask the user if they want to enter another set of questions and choices

#8. display exit message when the user is done with the program