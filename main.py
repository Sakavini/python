from exercises.functions import *

while True:
    welcome()
    option = input("Choose the desired option: ")
    if option == "1":
        clear_terminal()
        print("Stating the program in:")
        countdown(3)
        clear_terminal()
        break
    elif option == "2":
        clear_terminal()
        print("Exiting the program in:")
        countdown(3)
        exit("Program closed!")
    else:
        print("Invalid option! Please, choose 1 or 2!")
        print()

while True:
    try:
        first_number = int(input("Input the first number: "))
        break
    except ValueError:
        print("Please enter a valid integer!")
        print()

while True:
    try:
        second_number = int(input("Input the second number: "))
        break
    except ValueError:
        print("Please enter a valid integer!")
        print()

valid_operators = ["+", "-", "*", "/"]
while True:
    operators = input("Choose an operator (+ - * /): ")
    if operators in valid_operators:
        break
    else:
        print("Please, enter a valid operator!")
        print()

sum = first_number + second_number
sub = first_number - second_number
mul = first_number * second_number
div = first_number / second_number

match operators:
    case "+":
        print(f"The sum between {first_number} and {second_number} is: {sum}")
    case "-":
        print(f"The sub between {first_number} and {second_number} is: {sub}")
    case "*":
        print(f"The mul between {first_number} and {second_number} is: {mul}")
    case "/":
        print(f"The div between {first_number} and {second_number} is: {div}")
    case _:
        print("Invalid operation!")
