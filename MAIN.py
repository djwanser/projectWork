# Dylan Wanser
# Integration Project Stage 1
# A haphazard amalgamation of what I have learned so far

print("My creator is named Dylan!")
print("I took him way too long to make, but he's proud of his project.")
print("Which option would you like to explore today?")
print("1. Quiz")
print("2. Jokes")
print("3. Grading Tool")
print("4. Mad Lib")
choice = int(input())
if choice == 1:
    print("Welcome to the quiz!")
    print("This part isn't finished yet because there are many questions to be written but, ")
    print("It won't take long to finish!")
elif choice == 2:
    print("Welcome to the Jokes application!")
    jokeChoice = int(input("Please pick a number between 1 and 4!"))
    if(jokeChoice == 1):
        print("I invented a new word!")
        print("Plagiarism")
    elif(jokeChoice == 2):
        print("Why do we tell actors to break a leg?")
        print("Because every play has a cast.")
    elif(jokeChoice == 3):
        print("Hear about the new restaurant called Karma?")
        print("There’s no menu: You get what you deserve.")
    else:
        print("Did you hear about the cornstalk who competed in the olympics?")
        print("He did a-MAIZE-ing")
elif choice == 3:
    print("Welcome to the grading tool!")
    correct = int(input("Enter questions correct: "))
    possible = int(input("Enter possible correct: "))
    gradeOne = (correct / possible)
    grade = (gradeOne * 100)
    print(grade)
    if(grade < 0 or grade > 100):
        print("Grade not within accepted values")
    elif grade >= 90:
        print("Very good!")
    elif grade >= 80:
        print("Good")
    elif grade >= 70:
        print("Fair")
    elif grade >= 60:
        print("Satisfactory.")
    else:
        print("Poor")
else:
    print("Welcome to Mad Libs!")
    print("Unfortunately I haven't written a madlib yet either.")
    print("But you can't rush art!")
