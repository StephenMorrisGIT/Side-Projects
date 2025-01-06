# choices.py

import csv

def get_valuation_method():
    choices = {}
    with open('stockValuationMethods.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            choices[i+1] = row

    print("Choose a stock valuation method:")
    for key, value in choices.items():
        print(f"{key}. {value[0]}")

    print() # spacing

    while True:
        user_input = input("Enter the number of your choice: ")
        if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
            selected_choice = int(user_input)
            print(f"You selected: \033[94m{choices[selected_choice][0]}\033[0m")
            return choices[int(user_input)][1]
        else:
            print("Invalid input. Please try again.")

