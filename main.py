import time

def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, how are you?")

def get_user_age():
    return int(input("What is your age?: "))

def print_menu():
    print("Options: ")
    print("(1)Market\n(2)Starbucks\n(3)Gas station\n(4)Exit")

def ask_option():
    return int(input("Select an option: "))

def confirm_option(num):
    print("You have picked " + str(num) + ".")

def run_menu(answer):
    if answer == 1:
        print("You want to go to the market.")
    elif answer == 2:
        print("You want to go to Starbucks.")
    elif answer == 3:
        print("You want to go to the gas station.")
    elif answer == 4:
        print("Bye, dont come back")
    else:
        answer = int(input("Select a number between 1 and 4: "))
    return answer





def main():
    user_name = get_user_name()
    greet_user(user_name)
    user_age = get_user_age()
    print_menu()
    option = ask_option()
    confirm_option(option)

    while option !=4:
        run_menu(option)
        if option != 4:
            option = ask_option()
            confirm_option(option)


if __name__ == "__main__":
    main()

## Made the chatbot code for prework
