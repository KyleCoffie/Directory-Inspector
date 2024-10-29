
# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.
# Code Example:
import os
path = input("What directory would you like the contents of? ")  

def list_directory_contents(path):
    try:
        print (os.listdir(path))
    
    except FileNotFoundError:
        print("Could not find a directory with that name")
    
list_directory_contents(path)


# List and print all files and subdirectories in the given path


# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories