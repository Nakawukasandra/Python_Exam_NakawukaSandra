#a)(i) As a python student, write a program using functions and conditions to display the grades that the students will be receiving.

def calculateGrades():
    print("\n...Student Grade Calculations...")

    try:
        mark = int(input('Enter mark scored:\t'))

        if 90 <= mark <= 100:
            print("Grade is A")
        elif 80 <= mark <= 89:
            print("Grade is B")
        elif 70 <= mark <= 79:
            print("Grade is C")
        elif 60 <= mark <= 69:
            print("Grade is D")
        elif 50 <= mark <= 59:
            print("Grade is E")
        else:
            print("Fail")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

calculateGrades()



