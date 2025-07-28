from pynput.keyboard import Key, Controller
from datetime import datetime
import pyinputplus as pyip
import time
import os


timerequest,inputrequest,running="NOT SET","NOT SET",True


logo=("""
 _____ _____ _   _ _  __    _    ____ _____  
|_   _| ____| | | | |/ /   / \  / ___|_   _| 
  | | |  _| | |_| | ' /   / _ \ \___ \ | |   
  | | | |___|  _  | . \  / ___ \ ___) || |   
  |_| |_____|_| |_|_|\_\/_/   \_\____/ |_|   
""")

#Variables set now to avoild calling issue later.

keyboard = Controller()

#Variable for pynputplus function unknown.

def setup ():

    global inputrequest,timerequest

    #Setting global variables to change the preset placeholders outside.

    inputrequest=input("\nPlease press the letter or key you want to be pressed (Example the spacebar) : ")

    while len(inputrequest) != 1:
        print("\nYou can only select a single key to be pressed")
        inputrequest=input("\nPlease press the key you want to be pressed (Example the spacebar) : ")

    # Input validation forces reply to be a single key press by checking length of answer given.

    timerequest = pyip.inputInt(prompt="\nHow often should the button be pressed? (Time in seconds): ")

    # Input validtion pyinputplus foring to be a int

    mainmenu()



def run():
    while running == True:

        #Sloppy creates endless loop but want to run forever so achives goal.
                
        keyboard.press(inputrequest)
        keyboard.release(inputrequest) 

        # Pynputplus needs to press and release the key 2 commands to get a key to activate

        if inputrequest == " ":
            print(f"{datetime.now()} Spacebar pressed ")
        else:
            print(f"{datetime.now()} {inputrequest} key pressed ")

        # datetime prints the Time now but unhappy adds so many micro seconds.

        time.sleep(timerequest)

        # Adds a delay for given time input



def info():
    print("""\nCreated by Bruce
          
          This was orginally just something to stop from timing out in World Of Warcraft.
          Added user input to allow custom keys and expand the fuction outside, idea being 
          in the world of working from home bosses want you at your PC every second of the day
          god forbid you take a piss.
          
          Also used as a learning op main things taken from project
          - User Input and input validation
          - Time function to add a pause
          - Formatting, not used in final version as not compatible with CMD
          
          Changes would make given if redone or wanted to focus more would expand options to
          add strings of keys rather then just a single key.
          Also would add change from seconds to minutes not sure what is more needed best have
          both options.
          
          Welcome any feedback or bug reports Tehkast@gmail.com""")
        
    print(logo)
    
    farts=input("Press any key to return to main menu: ")

    mainmenu()



def mainmenu():

    os.system('cls')
    #os.system('clear')

    print("""\n
 █████╗ ███████╗██╗  ██╗
██╔══██╗██╔════╝██║ ██╔╝
███████║█████╗  █████╔╝ 
██╔══██║██╔══╝  ██╔═██╗ 
██║  ██║██║     ██║  ██╗
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ Check \n""")

    print("1. Setup")
    print("2. Run")
    print("3. Info")
    if inputrequest == " ":
        print(f"\nCurrent Settings Press Spacebar every {timerequest} seconds.")
    else:
        print(f"\nCurrent Settings Press {inputrequest} every {timerequest} seconds.")
    print("\nFuck the bosses - Jimmy Mcnulty 2004 \n")
    


    selection = pyip.inputNum("Please enter the number of your selection: ", min=1, lessThan=4)

    if selection == 1:
        setup()
    elif selection == 2:
        if inputrequest == "NOT SET":
            print("\nNeed to set variable.")
            setup()
        elif timerequest == "NOT SET":
            print("\nNeed to set variable.")
            setup()
        else:
            print("CLOSE WINDOW TO STOP RUNNING")
            run()
    elif selection ==3:
        info()

    print("\n")

    

mainmenu()

