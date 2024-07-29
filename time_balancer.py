import sys, time
from pathlib import Path

# Print the main menu
def MainMenu():
    # Get input
    while(True):
        time.sleep(0.5)
        print("---\nYou have x amount of gametime\n---") # To be changed later
        print(" Please select an option:")
        print(" 1. Start gametime")
        print(" 2. Log gametime")
        print(" 3. Start non-gametime")
        print(" 4. Log non-gametime")
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
            Gametime()
        elif selection == 2:
            print("[Log gametime]")
        elif selection == 3:
            NonGametime()
        elif selection == 4:
            print("[Log non-gametime]")
        elif selection == 9:
            print("[Settings]")
        elif selection == 0:
            sys.exit()
        else:
            print("Error: invalid input")


# Get config file directory
def GetDirectory():
    if (sys.platform == "win32"):
        DIRECTORY = Path.home() / "AppData/Local/time_balancer"
        if (not DIRECTORY.exists()):
            DIRECTORY.mkdir()
        return DIRECTORY
    
    elif (sys.platform == "darwin"):
        DIRECTORY = Path("/Library/Caches/time_balancer")
        if (not DIRECTORY.exists()):
            DIRECTORY.mkdir()
        return DIRECTORY
        # TODO: Make sure mac stuff works
    
    elif (sys.platform == "linux"):
        # TODO: Make linux stuff
        pass
    
    else:
        raise Exception("Unrecognised operating system")


def ReadData():
    pass


# Writes the gametime and non-gametime to a text file
def WriteData(gameTime = 0, nonGameTime = 0):
    DIRECTORY = GetDirectory()
    TIMES_FILE_DIR = DIRECTORY / "times.txt"

    FILE = open(TIMES_FILE_DIR, "w")
    FILE.write(str(int(gameTime)) + "\n" + str(int(nonGameTime)))
    FILE.close()


# Turns every 15 mins into a string of '#'
def MakeTimeBar(seconds):
    numHashes = int(seconds) / 900
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
    return timeDifference


def Gametime():
    print("Starting timer for gametime")
    timeSpent = StartTimer()

    ReadData()
    # TODO: Read existing times, calculate into new variables

    WriteData(gameTime = timeSpent)
    # Write timeSpent to times.txt


def NonGametime():
    print("Starting timer for non-gametime")
    timeSpent = StartTimer()
    # Write timeSpent to AppData\Local


# Start of program
MainMenu()