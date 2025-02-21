def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]

def binary_to_hexadecimal(binary):
    decimal_value = binary_to_decimal(binary)
    hexadecimal_value = hex(decimal_value)[2:].upper()
    return hexadecimal_value

def decimal_to_hexadecimal(decimal):
    return hex(int(decimal))[2:].upper()

def hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

def hexadecimal_to_binary(hex_str):
    decimal_value = hexadecimal_to_decimal(hex_str)
    return bin(decimal_value)[2:]

def octal_to_decimal(octal_str):
    return int(octal_str, 8)

def decimal_to_octal(decimal):
    return oct(int(decimal))[2:]

def octal_to_hexadecimal(octal_str):
    decimal_value = octal_to_decimal(octal_str)
    return hex(decimal_value)[2:].upper()

def get_valid_number(prompt, valid_chars):

    while True:
        value = input(prompt).strip()
        if all(char in valid_chars for char in value):
            return value
        else:
            print(f"Invalid input! Please enter a number using {valid_chars}.")

def main():
    print("Welcome to the Number Conversion Program!")

    while True:
        print("\nChoose a number conversion:")
        print("(1) Binary to Decimal")
        print("(2) Decimal to Binary")
        print("(3) Binary to Hexadecimal")
        print("(4) Decimal to Hexadecimal")
        print("(5) Hexadecimal to Decimal")
        print("(6) Hexadecimal to Binary")
        print("(7) Octal to Decimal")
        print("(8) Decimal to Octal")
        print("(9) Octal to Hexadecimal")

        choice = input("Enter choice 1-9: ").strip()

        if choice == "1":
            binary = get_valid_number("Enter a valid Binary number: ", "01")
            decimal = binary_to_decimal(binary)
            print(f"Binary: {binary}  Decimal: {decimal}")

        elif choice == "2":
            decimal = get_valid_number("Enter a valid Decimal number: ", "0123456789")
            binary = decimal_to_binary(decimal)
            print(f"Decimal: {decimal}  Binary: {binary}")

        elif choice == "3":
            binary = get_valid_number("Enter a valid Binary number: ", "01")
            hexadecimal = binary_to_hexadecimal(binary)
            print(f"Binary: {binary}  Hexadecimal: {hexadecimal}")

        elif choice == "4":
            decimal = get_valid_number("Enter a valid Decimal number: ", "0123456789")
            hexadecimal = decimal_to_hexadecimal(decimal)
            print(f"Decimal: {decimal}  Hexadecimal: {hexadecimal}")

        elif choice == "5":
            hex_val = get_valid_number("Enter a valid Hexadecimal number: ", "0123456789ABCDEFabcdef")
            decimal = hexadecimal_to_decimal(hex_val)
            print(f"Hexadecimal: {hex_val}  Decimal: {decimal}")

        elif choice == "6":
            hex_val = get_valid_number("Enter a valid Hexadecimal number: ", "0123456789ABCDEFabcdef")
            binary = hexadecimal_to_binary(hex_val)
            print(f"Hexadecimal: {hex_val}  Binary: {binary}")

        elif choice == "7":
            octal = get_valid_number("Enter a valid Octal number: ", "01234567")
            decimal = octal_to_decimal(octal)
            print(f"Octal: {octal}  Decimal: {decimal}")

        elif choice == "8":
            decimal = get_valid_number("Enter a valid Decimal number: ", "0123456789")
            octal = decimal_to_octal(decimal)
            print(f"Decimal: {decimal}  Octal: {octal}")

        elif choice == "9":
            octal = get_valid_number("Enter a valid Octal number: ", "01234567")
            hexadecimal = octal_to_hexadecimal(octal)
            print(f"Octal: {octal}  Hexadecimal: {hexadecimal}")

        else:
            print("Invalid choice. Please select 1-9.")

        exit_prompt = input("\nType 'yes' to exit or press Enter to continue: ").strip().lower()
        if exit_prompt == "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()