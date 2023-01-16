from art import logo
print(logo)
 
def add(n1, n2):
    return n1 + n2
 
def subtract (n1, n2):
    return n1 - n2
 
def multiply(n1, n2):
    return n1 * n2
 
def divide(n1, n2):
    return n1 / n2
 
operations = {
    "+" : add,
    "-" : subtract, 
    "*" : multiply, 
    "/" : divide
    }
 
def start_new():
    number = int(input("What is the first number? "))
 
    for operation in operations:
        print(operation)
    return number
 
num1 = start_new()
 
keep_calculating = True
while keep_calculating:
    operation_symbol = input("Pick an operation form the list above: ")
    num2 = int(input("What is the next number? "))
 
    answer = operations[operation_symbol](num1, num2)
 
    print(f"{num1} {operation_symbol} {num2} = {answer}")
 
    keep_going = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ")
    if keep_going == 'e':
        keep_calculating = False
    elif keep_going == 'n':
        num1 = start_new()
    else:
        num1 = answer