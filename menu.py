
def getNumber():
    userNum = int(input("Enter a number: "))
    #do validation
    return userNum

def displayMenu():

    def print_menu():
        print(30 * "-", "NUMERIC OPERATIONS MENU", 30 * "-")
        print("1. Enter a number ")
        print("2. Add numbers ")
        print("3. Average numbers ")
        print("4. Placeholder ")
        print("5. Exit from the script ")
        print(85 * "-")

    loop = True
    userInput = -1
    userInputList = []

    while loop:  # While loop which will keep going until loop = False
        print_menu()  # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            choice = ''
            userInput = getNumber()
            print("userInput: ", userInput)
            userInputList.append(userInput)
            print("userInputList: ", userInputList)
        elif choice == '2':
            if len(userInputList) >= 1:
                print("Numbers to add: ", userInputList)
                another = True
                while another:
                    promptForAnother = input("Enter another number?  (y or n) ")
                    if promptForAnother == 'y':
                        userInputList.append(getNumber())
                        print("userInputList: ", userInputList)
                    else:
                        another = False
                print("Sum: ", sum(userInputList))
            else:
                print("You can't do that until you enter a number.  Please choose menu option 1 to enter a number.")
        elif choice == '3':
            print("you have selected option 3")
            if len(userInputList) >= 1:
                print("Numbers to average: ", userInputList)
                another = True
                while another:
                    promptForAnother = input("Enter another number?  (y or n) ")
                    if promptForAnother == 'y':
                        userInputList.append(getNumber())
                        print("userInputList: ", userInputList)
                    else:
                        another = False
                print("Average: ", sum(userInputList)/len(userInputList))
            else:
                print("You can't do that until you enter a number.  Please choose menu option 1 to enter a number.")

        elif choice == '4':
            print("you have selected option 4")
        elif choice == '5':
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return 0


print(displayMenu())