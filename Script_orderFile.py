"""Main"""


"""Imports"""
import os
from pathlib import Path
import time
import json
"""System variables"""

"""Functions"""

def show_menu():
    print("Type /create_file (for create the file)")
    print("Type /write_file (for write something inside a file)")
    print("Type /delete_file (for delete the file)")
    print("Type /read_file (for read a file)")
    print("Type /clean_file (for delete everything inside the file)")
    print("Type /open_file (for open the file)")
    print("Type /verify_file (for check the exstension of a file or if the file exists)")
    print("Type /show_files (for show the files in the directory)")
    print("Type /rename_file (for rename the file)")
    print("Type /quit for close the program")
    
def separator(caracter = "-"):
    try:
        lenght = os.get_terminal_size().columns
    except OSError:
        lenght = 80

    print(caracter * lenght)

def create_file(path):
    file = Path(path)
    extension = file.suffix.lower()
    if not os.path.exists(file):
        if extension == ".txt":
            try:
                with open(path, "w") as file:
                    pass
                print("File created!")
            except:
                print("ERROR while creating text file!")
        elif extension == ".json":
            try:
                with open(path, "w") as file:
                    json.dump([], file)
                print("File created!")
            except:
                print("ERROR while creating json file")
        else:
            print("ERROR: extension not found!")
    else:
        print("ERROR: file alredy exist!")

def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print("File removed!")
        except:
            print(f"ERROR while removing {path}")
    else:
        print("ERROR: file doesn't exists!")

def read_file(path):
    if os.path.exists(path):
        file = Path(path)
        extension = file.suffix.lower()
        if extension == ".txt":
            try:
                with open(file, "r") as file:
                    found = file.read()
                
                print(f"Here is what I found: \n{found}\n")
                separator()
            except:
                print("ERROR while reading text file")
        elif extension == ".json":
            if os.path.getsize(file) == 0:
                print("ERROR: file empty!")
            else:
                try:
                    with open(file, "r") as file:
                        found = json.load(file)
                    print(f"Here is what I found: \n{found}\n")
                    separator()
                except:
                    print("ERROR while reading a json file!")
        else:
            print("ERROR: extension not found!")
            print("Trying again...")
            time.sleep(0.55)
            try:
                with open(file, "r") as file:
                    found = file.read()
                print(f"Here is what I found: \n{found}\n")
                separator()
            except:
                print(f"ERROR while trying to read {path} (AGAIN!)")
    else:
        print("ERROR: file not found!")

def write_file(path):
    if os.path.exists(path):
        content = input("Type here what you would like to write in the file: ")
        file = Path(path)
        extension = file.suffix.lower()
        if extension == ".txt":
            try:
                with open(file, "w") as file:
                    file.write(content + "\n")
                print("File written!")
            except:
                print("ERROR while writing text file!")
        elif extension == ".json":
            try:
                with open(file, "w") as file:
                    json.dump({"Content": content}, file, indent=1)
                print("File written!")
            except:
                print("ERROR while writing json file!")
        else:
            print("ERROR: extension not found!")
            print("Trying again...")
        time.sleep(0.55)
        try:
            with open(file, "w") as file:
                file.write(content + "\n")
            print("File written!")
        except:
            print(f"ERROR while writing {path} (AGAIN!)")
    else:   
        print("ERROR: file doesn't exists!")

def empty_file(path):
    file = Path(path)
    extension = file.suffix.lower()
    if os.path.exists(file):
        if extension == ".txt":
            try:
                with open(path, "w") as file:
                    pass
                print("File cleaned!")
            except:
                print("ERROR while cleaning text file!")
        elif extension == ".json":
            try:
                with open(path, "w") as file:
                    json.dump([], file)
                print("File cleaned!")
            except:
                print("ERROR while cleaning json file")
        else:
            print("ERROR: extension not found!")
    else:
        print("ERROR: file not found!")

def open_file(path):
    if os.path.exists(path):
        try:
            os.startfile(path)
            print("File opened!")
        except:
            print("ERROR while opening file!")
    else:
        print("ERROR: file not found!")

def verify_file(path):
    file = Path(path)
    extension = file.suffix.lower()
    action = print("What you would like to verify?\n /file_exists (check if the file exists)\n /file_extension (check the extension of the file)")
    action = input("Type the command: ")
    if action == "/file_exists":
        print("Checking in the file exists...")
        try:
            if os.path.exists(file):
                print("File exists!")
            else:
                print("File doesn't exists!")
        except:
            print(f"Error while checking if {path} exists!")
    elif action == "/file_extension":
        print("Checking the file extension...")
        if os.path.exists(file):
            print(f"Extension = {extension}")
        else:
            print("ERROR: file not found!")

def show_all_file():
    try:
        os.system("dir")
    except:
        print("ERROR while tying to show content")

def rename_file(path):
    if os.path.exists(path):
        file_name = input("Type the new name for the file: ")
        try:
            os.rename(path, file_name)
            print(f"File name changed from {path} to {file_name}")
        except:
            print("ERROR while renaming the new file")
    else:
        print("ERROR: file doesn't exist")
                      
"""Script"""
while True:
    choosen_file = input("Type the name of the file: ")
    show_menu()
    action = input("Type here what you would like to do: ")
    if action == "/create_file":
        create_file(choosen_file)
    elif action == "/write_file":
        write_file(choosen_file)
    elif action == "/delete_file":
        delete_file(choosen_file)
    elif action == "/read_file":
        read_file(choosen_file)
    elif action == "/clean_file":
        empty_file(choosen_file)
    elif action == "/open_file":
        open_file(choosen_file)
    elif action == "/verify_file":
        verify_file(choosen_file)
    elif action == "/quit":
        print("Closing the program")
        time.sleep(0.15)
        quit()
    elif action == "cls":
        try:
            os.system("cls")
        except:
            print("ERROR while trying to clean the console")
    elif action == "/show_files":
        show_all_file()
    elif action == "/rename_file":
        rename_file(choosen_file)
    else:
        print("Going back to the menu...")
