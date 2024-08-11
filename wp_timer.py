
import sys
import time
from pathlib import Path
from os import system # Only used to clear cmdline


# Print the main menu
def main_menu():
    # Display menu
    while(True):
        time.sleep(0.5)

        work_time, modifier = read_data()

        print("-"*(24+len(str(work_time)))) # Adjusts bar to second line's length
        print(f"You have {work_time} minutes stored")
        print(":" + make_time_bar(work_time) + ":")
        print(f"Modifier is set to {modifier}")
        print("-"*(24+len(str(work_time))))

        print("Please select an option:")
        print(" 1. Start work time")
        print(" 2. Log work time")
        print(" 3. Start game time")
        print(" 4. Log game time")
        print(" 9. Change settings")
        print(" 0. Exit")
        
        # Parse input
        selection = input("> ")
        try:
            selection = int(selection)
        except:
            # Not a number
            pass

        # Interpret seletion to choice
        if selection == 1:
            work_time()
        elif selection == 2:
            log_work_time()
        elif selection == 3:
            game_time()
        elif selection == 4:
            log_game_time()
        elif selection == 9:
            change_settings()
        elif selection == 0:
            clear()
            sys.exit()
        else:
            print("Error: invalid input")


# Get config file directory
def get_directory():
    if (sys.platform == "win32"):
        DIRECTORY = Path.home() / "AppData/Local/wp_timer"
    
    elif (sys.platform == "darwin") or (sys.platform == "linux"):
        DIRECTORY = Path.home() / "Documents/wp_timer"
    
    else:
        try:
            DIRECTORY = Path.home() / "Documents/wp_timer"
        except:
            raise Exception("Unrecognised operating system")
    
    if (not DIRECTORY.exists()):
            # Make a blank file if it doesn't exist
            DIRECTORY.mkdir()
            TIMES_FILE_DIR = DIRECTORY / "times.txt"
            FILE = open(TIMES_FILE_DIR, "w")
            FILE.write("0\n1.0")
            FILE.close()
    
    return DIRECTORY


# Writes the gametime and non-gametime to a text file
def write_data(work_time, modifier):
    DIRECTORY = get_directory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "w")
    FILE.write(str(work_time) + "\n" + str(modifier))
    FILE.close()


# Reads the stored times, returns ints as gameTime, nonGameTime, modifier
def read_data():
    DIRECTORY = get_directory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "r")
    work_time = FILE.readline()
    modifier = FILE.readline()
    return int(work_time), float(modifier)


# Clears cmdline based on OS
def clear():
    if sys.platform == "win32":
        system('cls')
    else:
        system('clear')


# Turns every 15 mins into a string of '#'
def make_time_bar(minutes):
    # If positive, print hashes
    if (minutes > 1):
        num_hashes = int(minutes) / 15
        return ("#" * int(num_hashes))
    # If negative, print dashes
    elif (minutes < 1):
        num_hashes = int(abs(minutes)) / 15
        return ("-" * int(num_hashes))
    else:
        return ""


# Timer used for both game and break time
def start_timer():
    start_time = time.time()
    print("Timer started at " + time.ctime(start_time)[11:16]) # Display hr:m

    # Wait for input
    input("Press return to stop timer ")

    end_time = time.time()
    time_difference =  end_time - start_time

    clear()
    print("Timer lasted for " + str(int(time_difference / 60)) + " minutes")
    return int(time_difference / 60)


# Menu for starting work time
def work_time():
    clear()
    print("Starting timer for work time")
    time_spent = start_timer()

    # Read existing times, calculate into new variables
    work_time, modifier = read_data()

    # Calculate new times
    work_time += int(time_spent * modifier)
    print(f"You have earned {int(time_spent * modifier)} minutes of gametime")

    # Update times.txt with new values
    write_data(work_time, modifier)


# Menu for starting game time
def game_time():
    clear()
    print("Starting timer for game time")
    time_spent = start_timer()

    # Read existing times, calculate into new variables
    work_time, modifier = read_data()

    # Calculate new times
    work_time -= time_spent

    # Update times.txt with new values
    write_data(work_time, modifier)


# Log work time outside of the timer
def log_work_time():
    print("How much time do you want to add? (mins)")
    while(True):
        logged_time = input("> ")
        try:
            logged_time = int(logged_time)
            break
        except:
            print("Invalid input, please try again")

    # Read existing times, calculate into new variables
    work_time, modifier = read_data()

    # Calculate new times
    work_time += int(logged_time * modifier)
    print(f"{int(logged_time * modifier)} minutes of gametime added")

    # Update times.txt with new values
    write_data(work_time, modifier)


# Log game time outside of the timer
def log_game_time():
    print("How much time do you want to subtract? (mins)")
    while(True):
        logged_time = input("> ")
        try:
            logged_time = int(logged_time)
            break
        except:
            print("Invalid input, please try again")

    # Read existing times, calculate into new variables
    work_time, modifier = read_data()

    # Calculate new times
    work_time -= int(logged_time)

    # Update times.txt with new values
    write_data(work_time, modifier)


# Currently just changes the modifier value
def change_settings():
    work_time, modifier = read_data()
    print("-- Settings --")
    print(f"Modifier is currently set to {modifier}")
    print(f"Every 1 minute of work gives you {modifier} minute(s) of gametime")

    selection = input("Enter a new value for the modifier if you wish to change it, or press return to go back\n> ")
    if selection!= '':
        try:
            modifier = float(selection)
            write_data(work_time, modifier)
        except:
            print("Invalid input")
    
    clear()


# Start of program
main_menu()