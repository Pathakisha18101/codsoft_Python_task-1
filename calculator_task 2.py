def calculator():
    print("Welcome to the Calculator!")

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} × {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                result = num1 / num2
                print(f"{num1} ÷ {num2} = {result}")
        elif choice == '5':
            print("Exiting calculator...")
            break
        else:
            print("Invalid choice. Please try again.")

        print()


calculator()