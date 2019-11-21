# ----------------------------------------------- #
# Title:  Assignment 06
# Description: Working with functions, lists, and
#              dictionaries
# Change Log (Who, When, What)
# K Mueller, 11/21/2019, Created Script
# -------------------------------------------------#

# Data --------------------------------------------#

myList = []  # A Dictionary that acts as a 'table' of rows
dicRow = {}  # A row of data separated into elements of a dictionary {Task, Priority}
strFile = 'ToDoList.txt' # The name of the data file

# Presentation (Input/Output) ---------------------#

def OutputMenuItems():  # Display a menu of choices to the user

    print()
    print("Menu of Options")
    print("-" * 40)
    print("1) Add Item To List")
    print("2) Display Current List")
    print("3) Save To File And Exit The Program")
    print("-" * 40)

def AddItems():  # Get input from the user and show the individual entry in the list of dictionary rows

    strTask = input("Enter a task or household chore: ")
    strPriority = input("Enter the priority [low, medium, high] of the task: ")
    dicRow = {"Task":strTask, "Priority":strPriority}
    myList.append(dicRow)
    print("You entered.... ")
    for strTask, strPriority in dicRow.items():
        print(strTask, " = ", strPriority)

def DispItems():  # Show all entries in the list of dictionary rows

    for objRow in myList:
        print(objRow["Task"] + ' = ' + objRow["Priority"])

def ExpItems():  # Write entries to text file

    strFile = open('ToDoList.txt', "w")
    for objRow in myList:
        strFile.write(objRow["Task"] + ' = ' + objRow["Priority"] + "\n")
    strFile.close()

# Presentation (Input/Output) ---------------------#

# Main Body of Script -----------------------------#

loop = True

while loop:

    OutputMenuItems()  # Display menu to the user
    add = input("Which Option Would You Like To Perform? [1 to 3]: ")

    if add=="1":

        AddItems()  # Add entries to the list
        print("Your entries have been saved to the list.... ")

    elif add =="2":

        print("Your current inventory is: ")
        DispItems()  # Display the current list

    elif add =="3":

        ExpItems()  # Write list to text file
        print("Data saved to file.  You have exited the program.")

        break

    else:
        print("Not a valid selection.")

# Main Body of Script -----------------------------#