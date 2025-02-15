def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            print(f"{user_input} is a good number")
            return int(user_input)
        else:
            print("Invalid number, Please try again!")

def main():
    print("This program adds two numbers.")

    while True:
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")

        print("Let's do some adding!")
        print(f"{num1} + {num2} = {num1 + num2}")

        exit_prompt = input("Type 'yes' to end program:").strip().lower()
        if exit_prompt == "yes":
            print("Good bye!!")
            print("Come back with more numbers ")
            break


if __name__ == "__main__":
    main()