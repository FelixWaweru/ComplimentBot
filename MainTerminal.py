import ComplimentBot
import Deleter
import sys
import threading

header = open("Header.txt","r")
print("\n" + "\n" + header.read())

firstOption = "0: Launch Bot "
secondOption = "1: Launch Tweet Deleter "
thirdOption = "2: Exit/ Terminate Bot "
fourthOption = "3: Exit Terminal "
fifthOption = "4: Send Bulk Message to all followers"

def options():
    print("\n")
    print(firstOption + "\n" + secondOption + "\n" + thirdOption + "\n" + fourthOption + "\n" + fifthOption + "\n")

def terminalExecution():
    a = 1
    while a == 1:
        options()
        selection = input("Please select value of the function you wish to execute." + "\n" + "==>")
        #Bot launcher

        if selection == "0":
            print("You chose " + firstOption + "\n")
            print("Launching bot")
            try:
                botLaunch = threading.Thread(target=ComplimentBot.threader())
                botLaunch.start()
                print("Bot successfully launched.")
            except:
                print("Bot could not be launched. Please try again.")

        #Tweet Deleter
        elif selection == "1":
            print("You chose " + secondOption + "\n")
            print("Are you sure you want to delete some tweets?" + "\n")
            choice1 = input("y/n: ")
            if choice1 == "y" or choice1 == "Y":
                try:
                    print("Tweet deletion commencing.")
                    deleteTweet = threading.Thread(target=Deleter.startDeletion())
                    deleteTweet.start()
                except:
                    print("Tweets could not be deleted. Pls try again")
            elif choice1 == "n" or choice1 == "N":
                print("Cancelling tweet deletion.")

        #Bot Stopper
        elif selection == "2":
            print("You chose " + thirdOption + "\n")
            print("Are you sure you want to stop the bot?" + "\n")
            choice2 = input("y/n: ")
            if choice2 == "y" or choice2 == "Y":
                try:
                    ComplimentBot.exitBot()
                    print("Bot terminated successfully.")
                except:
                    print("Bot could not be terminated. Pls try again")
            elif choice2 == "n" or choice2 == "N":
                print("Cancelling bot termination")

        #Terminal Stopper
        elif selection == "3":
            print("You chose " + fourthOption)
            print("Are you sure you want to exit the terminal?" + "\n")
            choice3 = input("y/n: ")
            print(choice3)
            if choice3 == "y" or choice3 == "Y":
                print("Terminal ended successfully.")
                sys.exit(0)
            elif choice3 == "n" or choice3 == "N":
                print("Cancelling Terminal termination")

        elif selection == "4":
            print("You chose " + fifthOption + "\n")
            print("Are you sure you want to send bulk message to all followers?" + "\n")
            choice4 = input("y/n: ")
            if choice4 == "y" or choice4 == "Y":
                try:
                    print("Bulk messaging commencing.")
                    bulkDm = threading.Thread(target=ComplimentBot.directMessenger())
                    bulkDm.start()
                except:
                    print("Bulk messages could not be sent. Pls try again")
            elif choice4 == "n" or choice4 == "N":
                print("Cancelling bulk messaging.")
        else:
            options()
            print("Please input an appropriate value.")


terminalExecution()