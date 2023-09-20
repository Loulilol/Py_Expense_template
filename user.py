from PyInquirer import prompt
import csv

user_questions = [
     {
        "type":"input",
        "name":"name",
        "message":"What is your name ? ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    newUser = prompt(user_questions)
    with open("users.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([newUser['name']])
    print("User Added !")
    return True