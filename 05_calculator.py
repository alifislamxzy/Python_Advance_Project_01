def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

    while True: 
        try:
            # Get user input
            choice = input("\nEnter your choice (1/2/3/4/5): ")
            
            # Quit the program
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            # Validate input
            if choice not in ['1', '2', '3', '4']:
                print("Invalid input! Please choose a valid option.")
                continue

            # Get numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform calculations based on user input
            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error! Division by zero is not allowed.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Run the calculator
calculator()
