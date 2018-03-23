import ComplimentBot
import Deleter
import sys

header = open("Header.txt","r")
print("\n" + "\n" + header.read())

firstOption = "0: Launch Bot "
secondOption = "1: Launch Tweet Deleter "
thirdOption = "2: Exit/ Terminate Bot "
fourthOption = "3: Exit Terminal "
print(firstOption  + "\n" + secondOption  + "\n" + thirdOption  + "\n" + fourthOption + "\n")

def terminalExecution():
    a = 1
    while a == 1:
        selection = input("Please select value of the function you wish to execute." + "\n" + "==>")
        if selection == "0":
            print("You chose " + firstOption + "\n")
            print("Launching bot")
            try:
                ComplimentBot.threader()
                print("Bot successfully launched.")
            except:
                print("Bot could not be launched. Please try again.")

        elif selection == "1":
            print("You chose " + secondOption + "\n")
            print("Are you sure you want to delete some tweets?" + "\n")
            choice = input("y/n: ")
            if choice is "y" or "Y":
                try:
                    print("Tweet deletion commencing.")
                    Deleter.startDeletion()
                except:
                    print("Tweets could not be deleted. Pls try again")
            elif choice is "n" or "N":
                print("Cancelling tweet deletion.")

        elif selection == "2":
            print("You chose " + thirdOption + "\n")
            print("Are you sure you want to stop the bot?" + "\n")
            choice = input("y/n: ")
            if choice is "y" or "Y":
                try:
                    ComplimentBot.exitBot()
                    print("Bot terminated successfully.")
                except:
                    print("Bot could not be terminated. Pls try again")
            elif choice is "n" or "N":
                print("Cancelling bot termination")

        elif selection == "3":
            print("You chose " + fourthOption)
            print("Are you sure you want to exit the terminal?" + "\n")
            choice = input("y/n: ")
            if choice is "y" or "Y":
                print("Terminal ended successfully.")
                sys.exit()

            elif choice is "n" or "N":
                print("Cancelling Terminal termination")

        else:
            print("Please input an appropriate value.")


terminalExecution()