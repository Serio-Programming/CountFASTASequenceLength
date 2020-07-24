# CountFASTASequences
# This program takes a FASTA file and counts the sequence lengths
# Output is recorded in a tabular format with query IDs in the first column
# And sequence lengths in the second column
# A program by Tyler Serio
# Circa May 2020

import os
import os.path
from os import path

def Count_Sequence_Lengths():
    # Ask for a file
    opening = 1
    while opening == 1:
        print("What file would you like to count sequences from?")
        print ("Example: 'fasta_file.fasta'")
        print ("Type the name of the file you would like to use,")
        fasta_file = input ("or type [0] to return to the menu. ")
        print ("")
        if fasta_file == "0":
            break

        # Check to see if the file exists
        path.exists(fasta_file)

        # If the file exists, move on to the next step
        if path.exists(fasta_file) == True:
            print("I will retrieve your file.")
            print("I have found your file.")
            fasta_file_name = fasta_file
            fasta_file = open(fasta_file, "r")
            opening = 0
            break

        # If the file doesn't exist, ask the User for another file name
        if path.exists(fasta_file) == False:
            print ("I will retrieve your file.")
            print ("I cannot find this file. Make sure to type the file name exactly.")
            print ("Try again, or type [0] to return to the menu.")
            print ("")
            opening = 1

    naming = 1
    while naming == 1:
        print("")
        print("Your output file will be saved as a text document.")
        print("You do not have to add an extension to your output file name.")
        output_file = input ("What would you like to name your output file? ")
        output_file = str(output_file)
        output_file = (output_file + ".txt")
        print("Your new file name is " + str(output_file))
        output_file = open(output_file, "w")
        print("")
        naming = 0
        break

    linec = 0
    linecount = 0
    for line in fasta_file:
        linec += 1
        if linec == 1:
            query = line.strip()
        if linec == 2:
            linecount = len(line) - 1
            output_file.write(query + "\t" + str(linecount) + "\n")
            output_file.flush()
            linec = 0

# Start the program
running = 1
while running == 1:
    # Display selections for the User to choose from
    print("Hello, what would you like to do?")
    print("")
    print("[1] - Count sequence lengths of a FASTA file.")
    print("[0] - Exit")
    print("")
    
    # Ask the User for selection input
    selecting = 1
    while selecting == 1:
        selection = 0
        selection = input("Which option do you choose? ")
        print("")
        if (selection != "1" and selection != "0"):
            if selection == "":
                selection = "Nothing"
            print("You have chosen [" + str(selection) + "].")
            print("That is not a proper selection.")
            print("Please choose from the list of selections.")
        else:
            selecting = 0

    # Begin counting lengths if selection is 1
    if selection == "1":
        Count_Sequence_Lengths()
        selection = 0

    # Exit the program if selection is 2
    if selection == "0":
        selecting = 2
        while selecting == 2:
            print ("Goodbye. Are you sure you want to exit?")
            print("")
            print("[y] - Yes")
            print("[n] - No")
            print ("")
            selection = input ("Which do you choose? ")
            print("")
            if (selection != "y" and selection != "n"):
                if selection == "":
                    selection == ("Nothing")
                print ("You have chosen [" + selection + "].")
                print ("That is not a proper selection.")
                print ("Please choose from the list of selections.")
            if selection == "y":
                exit()
            if selection == "n":
                print ("Oops. Nevermind then.")
                selecting = 0 
