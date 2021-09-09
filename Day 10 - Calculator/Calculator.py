import art

print(art.logo)
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b 


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():

    num1 = float(input("Enter the first number     "))


    should_continue = True

    while should_continue:
        for operation in operations:
            print(operation)
        selected_operation = input("Pick an operation")

        num2 = float(input("Enter the next number:   "))

        calculation_function = operations[selected_operation]


        answer = calculation_function(num1, num2)

        print(f"{num1} {selected_operation} {num2}  = {answer}\n")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation, or type 'e' to exit")
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            calculator()
        else:
            should_continue = False

calculator()