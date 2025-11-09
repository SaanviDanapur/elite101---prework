import time
import random


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, how are you?")

def get_user_age():
    return int(input("What is your age?: "))

def print_menu():
    print("Options: ")
    print("(1)Tic Tac Toe\n(2)Rock Paper Scissors\n(3)Mad Libs\n(4)Exit")

def ask_option():
    return int(input("Select an option: "))

def confirm_option(num):
    print("You have picked " + str(num) + ".")

def rock_paper_scissors():
    action_list = ['rock', 'paper', 'scissors']

    print("There will be three rounds")
    print("The best of three wins!!")

    count = 0

    for i in range(3):
        user_turn = int(input("Pick (1) rock, (2) paper, (3) scissors: "))
        user_turn = action_list[user_turn - 1]
        print(f'You have picked {user_turn}')
        program_turn = random.choice(action_list)
        print(f'The program picked {program_turn}')
        if user_turn == program_turn:
            print("You tied")
        elif (user_turn == 'paper' and program_turn == 'rock') or (user_turn == 'rock' and program_turn == 'scissors') or (user_turn == 'scissors' and program_turn == 'paper'):
            print('You won!!, you are now awarded one point')
            count += 1
        else:
            print('you lost!!')

    if count >= 2:
        print("You won rock paper scissors!!")
    else:
        print("You lost rock paper scissors. Better luck next time fine lad.")
        

def mad_libs():
    print('Welcome to Madlibs!')
    print("Now take somtime to fill in the following: ")
    variable1 = input("Enter an adjective: ")
    variable2 = input("Enter a plural creature: ")
    variable3 = input("Enter a mysterious object: ")
    variable4 = input("Enter a place: ")
    variable5 = input("Enter a main character: ")
    variable6 = input("Enter a past-tense verb: ")
    variable7 = input("Enter a tool or weapon: ")
    variable8 = input("Enter a descriptive of emotional adjective: ")
    variable9 = input("Enter a exclamation(ex. AHHH): ")
    variable10 = input("Enter a rival or villan name: ")
    variable11 = input("Enter an emotion: ")
    variable12 = input("Enter a a verb with an ing ending: ")
    variable13 = input("Enter a silly phrase: ")
    variable14 = input("Enter a everyday noun: ")
    variable15 = input("Enter a type of food or drink: ")


    print('Now you are able to choose between 3 story types')
    user_story = int(input("(1)Fantasy (2)Depressing (3)Science Fiction: "))

    if user_story == 1:
        print(f'In the {variable1} future, humanity finally made contact with the {variable2} of planet {variable4}. Captain {variable5} was chosen to deliver the {variable3}, a device said to control the fabric of time itself.\n')
        time.sleep(3)
        print(f'But the mission went wrong. The evil warlord {variable10} {variable6} the ship with a {variable7} beam, causing chaos across the stars. “{variable9}!” shouted {variable5} as alarms blared and the crew began {variable12} wildly.\n')
        time.sleep(3)        
        print(f'In the end, only {variable11} could save the galaxy. With a single act of courage and a ration of {variable15}, Captain {variable5} restored order to the cosmos — and left behind a legend written in {variable14} and starlight.\n')
        time.sleep(3)


    elif user_story == 2:
        print(f'It was another {variable1} morning in {variable4}. {variable5} sat alone, staring at the {variable3} on the table — once important, now just another piece of {variable14} collecting dust.\n')
        print(f'Outside, the {variable2} made their usual noise, but even that sounded tired. {variable5} {variable6} the old {variable7} out of habit, though there was nothing left to fix, nothing left to fight.\n')
        print(f'Sometimes they whispered “{variable9}” to the empty air, pretending someone might answer. The {variable8} light through the window didn’t warm them anymore — it only reminded them of what was gone.\n')
        print(f'Still, they kept {variable12}, kept waiting, because that’s what people do when {variable11} becomes the only thing left. Dinner was just {variable15} again. The silence tasted the same as always.\n')
    
    elif user_story == 3:
        print(f'Long ago, in the {variable1} realm of {variable4}, the noble hero {variable5} was chosen to recover the stolen {variable3} from the dark sorcerer {variable10}. Armed with only a {variable7} and unshakable {variable11}, they {variable6} forth across mountains haunted by {variable2}.\n')
        print(f'At the peak of the world, {variable5} faced {variable10} in an epic battle. “{variable9}!” cried {variable5} as sparks flew and the ground trembled. The duel lasted three days and nights, ending only when both warriors collapsed into fits of {variable12}.\n')
        print(f'Peace returned to {variable4}. At the feast of victory, the people toasted with {variable15} and cheered, “{variable13}!” as {variable5} raised the {variable14} high, forever remembered as the hero of the {variable8} age.\n')

    else:
        print("Sorry, try again later.")
    

def tic_tac_toe():
    
    p_o = input("Who will be naughts? ")
    p_x = input("Who will be crosses? ")
    print("Welcome "+p_o+" and "+p_x+"! 👋")


    print("-"*13)
    grid_index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"| {grid_index[0]}"+f" | {grid_index[1]} "+f" | {grid_index[2]} |")
    print("-"*13)
    print(f"| {grid_index[3]}"+f" | {grid_index[4]} "+f" | {grid_index[5]} |")
    print("-"*13)
    print(f"| {grid_index[6]}"+f" | {grid_index[7]} "+f" | {grid_index[8]} |")
    print("-"*13)

    turns = 0
    for turns in range(9):  
        input_symbol_1 = input(p_o+" , what symbol do you want to place? ")
        result_symbol_1 = ["o", "O"]
        while input_symbol_1 not in result_symbol_1:
            print("Error! Only Os are allowed "+p_o+" .")
            input_symbol_1 = input(p_o+" , what symbol do you want to place? ")
            if input_symbol_1 in result_symbol_1:
                continue;
        input_symbol_2 = input(p_x + " , what symbol do you want to place? ")
        result_symbol_2 = ["x", "X"]
        while input_symbol_2 not in result_symbol_2:
            print("Error! Only Xs are allowed "+p_o+".")
            input_symbol_2 = input(p_x+" , what symbol do you want to place? ")
            if input_symbol_2 in result_symbol_2:
                continue;
        print(grid_index)
        input_square_int_1 =int(input(p_o+", what square do you want? "))
        while input_square_int_1 not in grid_index:
            print("Your number should be less than or equal to 9!")
            input_square_int =int(input(p_o+", what square do you want? "))
            if input_square_int in grid_index:
                continue;
        grid_1 = input_square_int_1 - 1
        grid_index[grid_1] = input_symbol_1
        input_square_int_2 =int(input(p_x+", what square do you want? "))
        while input_square_int_2 not in grid_index:
            print("Your number should be less than or equal to 9!")
            input_square_int_2 =int(input(p_x + ", what square do you want? "))
            if input_square_int_2 in grid_index:
                continue;
        grid_2 = input_square_int_2 - 1
        grid_index[grid_2] = input_symbol_2

    print("-"*13)
    print(f"| {grid_index[0]}"+f"| {grid_index[1]} "+f"| {grid_index[2]} |")
    print("-"*13)
    print(f"| {grid_index[3]}"+f"| {grid_index[4]} "+f"| {grid_index[5]} |")
    print("-"*13)
    print(f"| {grid_index[6]}"+f"| {grid_index[7]} "+f"| {grid_index[8]} |")
    print("-"*13)
    
    turns += 1
    
    print(f"Thanks for playing {p_o} and {p_x} !😀")

#This took me way longer than it should've lol
    


def run_menu(answer):
    if answer == 1:
        tic_tac_toe()
    elif answer == 2:
        rock_paper_scissors()
    elif answer == 3:
        mad_libs()
    elif answer == 4:
        print("I hope you had a great time!")
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
            print_menu()
            option = ask_option()
            confirm_option(option)

# if __name__ == "__main__":
#     main()

## Made the chatbot code for prework
main()