# Function to add
def add(x, y):
    return x + y


# Function for subtraction
def subtract(x, y):
    return x - y


# Function for multiplication
def multiply(x, y):
    return x * y


# Function for dividing
def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter the operation number (1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using the calculator.")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    else:
        print("Wrong choice of operation")
