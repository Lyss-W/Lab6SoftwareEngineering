# Print menu
# Prompt user for input
#   1. Encode user input
#       -Intake 8 digit string
#       -Shift up each digit by 3 numbers
#       -Store encoded password
#       -Print Success Message
#   2. Decode user input
#       -
#   3. Quit
#       -Break

from encoder_file import encoder
from encoder_file import decoder

def main():
    while True:
        # Print Menu
        print(f"Menu")
        print(f"-------------")
        print(f"1. Encode")
        print(f"2. Decode")
        print(f"3. Quit")

        # Prompt user input
        user_input = int(input(f"\nPlease enter an option: "))

        # User Options
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encoder(password)
            print(f"Your password has been encoded and stored!\n")
        elif user_input == 2:
            password = input("Please enter your password to decode: ")
            decoded_pass = decoder(password)
            print(f"Your password has been encoded and stored!\n")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()
