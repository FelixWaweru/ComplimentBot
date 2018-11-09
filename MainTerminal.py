import ComplimentBot
import Deleter
import FollowAccounts
import sys
import threading

header = open("Header.txt","r")
print("\n" + "\n" + header.read())

firstOption = "0: Exit Terminal "
secondOption = "1: Launch Bot "
thirdOption = "2: Exit/ Terminate Bot "
fourthOption = "3: Launch Tweet Deleter "
fifthOption = "4: Send Bulk Message to all followers"
sixthOption = "5: Follow the followers of a specific user "

def options():
    print("\n")
    print(firstOption + "\n" + secondOption + "\n" + thirdOption + "\n" + fourthOption + "\n" + fifthOption + "\n" +
          sixthOption + "\n")

def terminalExecution():
    a = 1
    while a == 1:
        selection = input("Please select value of the function you wish to execute." + "\n" + "==>")

        # Exit Terminal
        if selection == "0":
            print("You chose " + firstOption)
            print("Are you sure you want to exit the terminal?" + "\n")
            choice3 = input("y/n: ")
            print(choice3)
            if choice3 == "y" or choice3 == "Y":
                print("Terminal ended successfully.")
                sys.exit(0)
            elif choice3 == "n" or choice3 == "N":
                print("Cancelling Terminal termination")

        # Bot Launcher
        elif selection == "1":
            print("You chose " + secondOption + "\n")
            print("Launching bot")
            try:
                botLaunch = threading.Thread(target=ComplimentBot.threader())
                botLaunch.start()
                print("Bot successfully launched.")
            except:
                print("Bot could not be launched. Please try again.")

        # Bot Stopper
        elif selection == "2":
            print("You chose " + thirdOption + "\n")
            print("Are you sure you want to stop the bot?" + "\n")
            choice2 = input("y/n: ")
            if choice2 == "y" or choice2 == "Y":
                try:
                    botLaunch.exit()
                    print("Bot terminated successfully.")
                except:
                    print("Bot could not be terminated. Pls try again")
            elif choice2 == "n" or choice2 == "N":
                print("Cancelling bot termination")

        # Tweet Deleter
        elif selection == "3":
            print("You chose " + fourthOption + "\n")
            print("Are you sure you want to delete some tweets?" + "\n")
            choice1 = input("y/n: ")
            if choice1 == "y" or choice1 == "Y":
                try:
                    print("Tweet deletion commencing.")
                    delete_tweet = threading.Thread(target=Deleter.startDeletion())
                    delete_tweet.start()
                except:
                    print("Tweets could not be deleted. Pls try again")
            elif choice1 == "n" or choice1 == "N":
                print("Cancelling tweet deletion.")

        # Bulk DMer
        elif selection == "4":

            # Sample DM
            # Stick around for some daily positivity or mention my username anywhere on Twitter and I'll tweet a compliment just for you :)

            print("You chose " + fifthOption + "\n")
            print("Are you sure you want to send bulk message to all followers?" + "\n")
            choice4 = input("y/n: ")
            if choice4 == "y" or choice4 == "Y":
                try:
                    print("Bulk messaging commencing.")
                    bulkDm = threading.Thread(target=ComplimentBot.direct_messenger())
                    bulkDm.start()
                except:
                    print("Bulk messages could not be sent. Pls try again")
            elif choice4 == "n" or choice4 == "N":
                print("Cancelling bulk messaging.")

        # Bulk Follower
        elif selection == "5":
            print("You chose " + sixthOption + "\n")
            username = input("Input the username of the person's followers you wish to follow:(Include the @ sign) ")
            print("Are you sure you want to follow " + str(username) + "'s followers?" + "\n")
            choice5 = input("y/n: ")
            if choice5 == "y" or choice5 == "Y":
                try:
                    print("Following commencing.")
                    bulkFollow = threading.Thread(target=FollowAccounts.follow(str(username)))
                    bulkFollow.start()
                except:
                    print("Users could not be followed. Pls try again")
            elif choice5 == "n" or choice5 == "N":
                print("Cancelling bulk following.")

        else:
            options()
            print("Please input an appropriate value.")


options()
terminalExecution()

