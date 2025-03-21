def enigma_calculator():
    print("Welcome to the Codebreaker's Calculator – The Enigma Device")
    print("Enter your calculations (e.g., 5 + 3). Type 'exit' to quit.")

    while True:
        # Get user input
        user_input = input("\n>>> ").strip()

        # Exit condition
        if user_input.lower() == "exit":
            print("Shutting down the Enigma Device. Mission Complete.")
            break

        try:
            # Evaluate the math expression safely
            result = eval(user_input, {"__builtins__": None}, {})

            # Display the result
            print(f"= {result}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception:
            print("Error: Invalid input. Please enter a valid math expression.")

# Run the calculator
enigma_calculator()
