import sys, os, time
from pathlib import Path

# Print the main menu
def MainMenu():
    # Display menu
    while(True):
        time.sleep(0.5)

        workTime, gameTime, modifier = ReadData()
        print(f"---\nWork time: {workTime} minutes\t" + MakeTimeBar(workTime))
        print(f"Game time: {gameTime} minutes\t" + MakeTimeBar(gameTime))
        print(f"Modifier is set to {modifier}\n---")

        print("Please select an option:")
        print(" 1. Start work time")
        print(" 2. Log work time")
        print(" 3. Start game time")
        print(" 4. Log game time")
        print(" 9. Change settings")
        print(" 0. Exit")
        
        # Parse input
        selection = input()
        try:
            selection = int(selection)
        except:
            # Not a number
            pass

        # Interpret seletion to choice
        if selection == 1:
            WorkTime()
        elif selection == 2:
            print("[Log work time]")
        elif selection == 3:
            GameTime()
        elif selection == 4:
            print("[Log game time]")
        elif selection == 9:
            ChangeSettings()
        elif selection == 0:
            sys.exit()
        else:
            print("Error: invalid input")


# Get config file directory
def GetDirectory():
    if (sys.platform == "win32"):
        DIRECTORY = Path.home() / "AppData/Local/work_and_play_timer"
    
    elif (sys.platform == "darwin"):
        DIRECTORY = Path("/Library/Application Support/work_and_play_timer")
    
    elif (sys.platform == "linux"):
        # TODO: Make linux stuff
        pass
    
    else:
        raise Exception("Unrecognised operating system")
    
    if (not DIRECTORY.exists()):
            # Make a blank file if it doesn't exist
            DIRECTORY.mkdir()
            TIMES_FILE_DIR = DIRECTORY / "times.txt"
            FILE = open(TIMES_FILE_DIR, "w")
            FILE.write("0\n0\n1.5")
            FILE.close()
    
    return DIRECTORY


# Writes the gametime and non-gametime to a text file
def WriteData(workTime, gameTime, modifier):
    DIRECTORY = GetDirectory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "w")
    FILE.write(str(workTime) + "\n" + str(gameTime) + "\n" + str(modifier))
    FILE.close()


# Reads the stored times, returns ints as gameTime, nonGameTime, modifier
def ReadData():
    DIRECTORY = GetDirectory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "r")
    workTime = FILE.readline()
    gameTime = FILE.readline()
    modifier = FILE.readline()
    return int(workTime), int(gameTime), float(modifier)


# Turns every 15 mins into a string of '#'
def MakeTimeBar(minutes):
    numHashes = int(minutes) / 15
    return ("#" * int(numHashes))


# Timer used for both game and break time
def StartTimer():
    startTime = time.time()
    print("Timer started at " + time.ctime(startTime)[11:16]) # Display hr:m

    # Wait for input
    input("Press return to stop timer")

    endTime = time.time()
    timeDifference =  endTime - startTime
    print("Timer lasted for " + str(int(timeDifference / 60)) + " minutes")
    return int(timeDifference / 60)


def WorkTime():
    print("Starting timer for work time")
    timeSpent = StartTimer()

    # Read existing times, calculate into new variables
    workTime, gameTime, modifier = ReadData()

    # Calculate new times
    workTime += timeSpent
    # TODO: subtract time x from time y using a modifiable value

    # Update times.txt with new values
    WriteData(workTime, gameTime, modifier)


def GameTime():
    print("Starting timer for game time")
    timeSpent = StartTimer()

    # Read existing times, calculate into new variables
    workTime, gameTime, modifier = ReadData()

    # Calculate new times
    gameTime += timeSpent
    # TODO: subtract time x from time y using a modifiable value

    # Update times.txt with new values
    WriteData(workTime, gameTime, modifier)


def ChangeSettings():
    workTime, gameTime, modifier = ReadData()
    print("-- Settings --")
    print(f"Modifier is currently set to {modifier}")
    print(f"Every {modifier} minutes of work gives you one minute of gametime")

    selection = input("Enter a new value for the modifier if you wish to change it, or press return to go back\n")
    if selection!= '':
        try:
            modifier = float(selection)
            WriteData(workTime, gameTime, modifier)
        except:
            print("Invalid input")


# Start of program
MainMenu()