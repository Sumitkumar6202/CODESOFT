#TASK 1- SIMPLE CALCULATOR
def calculator():
    # Prompt user for numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Prompt user to choose an operation
    print("\nChoose an operation:")
    print("Press 1 for addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division ")

    Operation = input("\nEnter the number of the operation (1/2/3/4): ")

    # Perform the selected operation
    if Operation == '1':
        Result = number1 + number2
        print(f"\nResult: {number1} + {number2} = {Result}")
    elif Operation == '2':
        Result = number1 - number2
        print(f"\nResult: {number1} - {number2} = {Result}")
    elif Operation == '3':
        Result = number1 * number2
        print(f"\nResult: {number1} * {number2} = {Result}")
    elif Operation == '4':
        if number2 != 0:  # Ensure no division by zero
            Result = number1 /number2
            print(f"\nResult: {number1} /{number2} = {Result}")
calculator()    
