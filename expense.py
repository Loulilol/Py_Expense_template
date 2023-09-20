from PyInquirer import prompt
import csv

def get_users():
    users = []
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                user = row[0]
                users.append(user)
    print(users)
    return users

def get_involved():
    involved = []
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                inv = row[0]
                involved.append({ 'name' : inv })
    print(involved)
    return involved

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_users()
    },
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved: ",
        "choices": get_involved()
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    #if not isinstance(infos['amount'], int):
    #    raise Exception("Expense Amount is not a number")
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open("expense_report.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([infos['amount'], infos['label'], infos['spender'], infos['involved']])
    print("Expense Added !")
    return True
