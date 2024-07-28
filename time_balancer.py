import sys, pathlib

# Print the main menu
def MainMenu():
    print("---\nYou have x amount of gametime\n---")
    print(" Please select an option:")
    print(" 1. Start gametime")
    print(" 2. Log gametime")
    print(" 3. Log non-gametime")
    print(" 4. Change settings")
    print(" 0. Exit")

    # Get input
    while(True):
        # Parse input
        selection = input()
        try:
            selection = int(selection)
        except:
            # Not a number
            pass

        # 
        if selection == 1:
            print("Selection 1")
            break
        elif selection == 2:
            print("Selection 2")
            break
        elif selection == 3:
            print("Selection 3")
            break
        elif selection == 4:
            print("Selection 4")
            break
        elif selection == 0:
            sys.exit()
        else:
            print("Error: invalid input")


# Start of program
MainMenu()

