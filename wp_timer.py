import sys, time
from pathlib import Path
from os import system # Only used to clear cmdline

# Print the main menu
def MainMenu():
    # Display menu
    while(True):
        time.sleep(0.5)

        workTime, modifier = ReadData()
        print("-"*26)
        print(f"You have {workTime} minutes stored")
        print(":" + MakeTimeBar(workTime) + ":")
        print(f"Modifier is set to {modifier}")
        print("-"*26)

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
            WorkTime()
        elif selection == 2:
            LogWorkTime()
        elif selection == 3:
            GameTime()
        elif selection == 4:
            LogGameTime()
        elif selection == 9:
            ChangeSettings()
        elif selection == 0:
            Clear()
            sys.exit()
        else:
            print("Error: invalid input")


# Get config file directory
def GetDirectory():
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
def WriteData(workTime, modifier):
    DIRECTORY = GetDirectory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "w")
    FILE.write(str(workTime) + "\n" + str(modifier))
    FILE.close()


# Reads the stored times, returns ints as gameTime, nonGameTime, modifier
def ReadData():
    DIRECTORY = GetDirectory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "r")
    workTime = FILE.readline()
    modifier = FILE.readline()
    return int(workTime), float(modifier)


# Clears cmdline based on OS
def Clear():
    if sys.platform == "win32":
        system('cls')
    else:
        system('clear')


# Turns every 15 mins into a string of '#'
def MakeTimeBar(minutes):
    # If positive, print hashes
    if (minutes > 1):
        numHashes = int(minutes) / 15
        return ("#" * int(numHashes))
    # If negative, print dashes
    elif (minutes < 1):
        numHashes = int(abs(minutes)) / 15
        return ("-" * int(numHashes))
    else:
        return ""


# Timer used for both game and break time
def StartTimer():
    startTime = time.time()
    print("Timer started at " + time.ctime(startTime)[11:16]) # Display hr:m

    # Wait for input
    input("Press return to stop timer ")

    endTime = time.time()
    timeDifference =  endTime - startTime

    Clear()
    print("Timer lasted for " + str(int(timeDifference / 60)) + " minutes")
    return int(timeDifference / 60)


# Menu for starting work time
def WorkTime():
    Clear()
    print("Starting timer for work time")
    timeSpent = StartTimer()

    # Read existing times, calculate into new variables
    workTime, modifier = ReadData()

    # Calculate new times
    workTime += int(timeSpent * modifier)
    print(f"You have earned {int(timeSpent * modifier)} minutes of gametime")

    # Update times.txt with new values
    WriteData(workTime, modifier)


# Menu for starting game time
def GameTime():
    Clear()
    print("Starting timer for game time")
    timeSpent = StartTimer()

    # Read existing times, calculate into new variables
    workTime, modifier = ReadData()

    # Calculate new times
    workTime -= timeSpent

    # Update times.txt with new values
    WriteData(workTime, modifier)


# Log work time outside of the timer
def LogWorkTime():
    print("How much time do you want to add? (mins)")
    while(True):
        loggedTime = input("> ")
        try:
            loggedTime = int(loggedTime)
            break
        except:
            print("Invalid input, please try again")

    # Read existing times, calculate into new variables
    workTime, modifier = ReadData()

    # Calculate new times
    workTime += int(loggedTime * modifier)
    print(f"{int(loggedTime * modifier)} minutes of gametime added")

    # Update times.txt with new values
    WriteData(workTime, modifier)


# Log game time outside of the timer
def LogGameTime():
    print("How much time do you want to subtract? (mins)")
    while(True):
        loggedTime = input("> ")
        try:
            loggedTime = int(loggedTime)
            break
        except:
            print("Invalid input, please try again")

    # Read existing times, calculate into new variables
    workTime, modifier = ReadData()

    # Calculate new times
    workTime -= int(loggedTime)

    # Update times.txt with new values
    WriteData(workTime, modifier)


# Currently just changes the modifier value
def ChangeSettings():
    workTime, modifier = ReadData()
    print("-- Settings --")
    print(f"Modifier is currently set to {modifier}")
    print(f"Every 1 minute of work gives you {modifier} minute(s) of gametime")

    selection = input("Enter a new value for the modifier if you wish to change it, or press return to go back\n> ")
    if selection!= '':
        try:
            modifier = float(selection)
            WriteData(workTime, modifier)
        except:
            print("Invalid input")
    
    Clear()


# Start of program
MainMenu()