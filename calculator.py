# Student Name: Justin Rich A. Galicha
# Course & Section: ITNT415
# Project: Calculator Master (TEST RUN)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a / b

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def display_menu():
    print("\n" + "="*30)
    print("      CALCULATOR MASTER      ")
    print("="*30)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*30)

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == '5':
            print("Exiting Calculator Master. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                except ZeroDivisionError as e:
                    print(e)
        else:
            print("Invalid choice! Please select a valid menu option (1-5).")

if __name__ == "__main__":
    main()
# Updated addition module validation
