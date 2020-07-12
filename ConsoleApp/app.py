import csv
import pandas
import csv


class Student:
    def __init__(self, email, name, address, course, fees):
        self.email = email
        self.name = name
        self.address = address
        self.course = course
        self.fees = fees

        with open('student.csv', 'a') as student_csv:
            writer = csv.writer(student_csv)
            writer.writerow([self.email, self.name, self.address, self.course, self.fees])


def get_email():
    email = input("Enter your email: ")
    return email


def get_name():
    name = input("Enter Your Name: ")
    return name


def get_address():
    address = input("Enter Your Address: ")
    return address


def course_select():
    course = int(input('''
    1. Press 1 for Python
    2. Press 2 for JavaScript
    3. Press 3 for React

    [Choose]  '''))

    if course == 1:
        return 'Python'
    elif course == 2:
        return 'JavaScript'
    elif course == 3:
        return 'React'
    else:
        print("Invalid Choice")


def get_balance():
    fee = int(input('''
    1. Press 1 to pay 20000
    2. Press 2 to pay 10000 only
    [Choose]  '''))

    if fee == 1:
        return 20000
    elif fee == 2:
        return 10000
    else:
        print("Invalid Choice")


def update_balance():
    fee = int(input('''
       1. Press 1 to pay remaining 10000
       2. Press 2 if paid 20000 already
       [Choose]  '''))

    if fee == 1:
        return 10000
    elif fee == 2:
        return 0
    else:
        print("Invalid Choice")


def course_inquiry():
    id = int(input('''
    
    1. Input 1 for Python Details
    2. Press 2 for JavaScript Details
    3. Press 3 for React Details
    4. Press 4 to get all subject details
    
    [Choose] '''))

    df = pandas.read_csv('courses.csv')
    if id < 4:
        print("\n", df.loc[df['Id'] == id], "\n")

    elif id == 4:
        print("\nAll Courses\n", df, "\n")
    else:
        print("Invalid Choice")


def student_registration():
    email = get_email()
    name = get_name()
    address = get_address()
    course = course_select()
    fees = get_balance()
    Student(email, name, address, course, fees)


def student_info():
    df = pandas.read_csv('student.csv')
    print("All students information \n\n", df)


def update_info():
    df = pandas.read_csv('student.csv')
    email = get_email()

    print('Enter Updated Values')
    name = get_name()
    address = get_address()
    course = course_select()
    balance = update_balance()
    df.loc[df['Email'] == email, 'Balance'] += balance
    df.loc[df['Email'] == email, 'Name'] = name
    df.loc[df['Email'] == email, 'Address'] = address
    df.loc[df['Email'] == email, 'Course'] = course

    df.to_csv('student.csv', sep=',', index=False)

    print("Your info is updated successfully")


def leave_incomplete():
    df = pandas.read_csv('student.csv', index_col='Email')
    email = get_email()
    df.drop([email], inplace=True)
    df.to_csv('student.csv', sep=',')
    print("You have successfully left the program ")


def return_deposit():
    df = pandas.read_csv('student.csv')
    email = get_email()
    df.loc[df['Email'] == email, 'Balance'] = 0
    df.to_csv('student.csv', sep=',', index=False)

    print("Congratulations for completing your course. Your deposit in returned to your account")
    print("Your Acoount Details \n", df.loc[df['Email'] == email], "\n")


def my_app(choice):
        if choice == 1:
            course_inquiry()
        elif choice == 2:
            student_registration()
        elif choice == 3:
            student_info()
        elif choice == 4:
            update_info()
        elif choice == 5:
            leave_incomplete()
        elif choice == 6:
            return_deposit()
        else:
            print("Invalid Argument")


choice = int(input('''
***********Welcome To MyApp**********

1. Press 1 for course detail
2. Press 2 to enroll in course
3. Press 3 to get all students details
4. press 4 to update student information
5. Press 5 to leave program without completion
6. Press 6 to complete and leave the program
7. Exit

[Choose]  '''))

my_app(choice)
