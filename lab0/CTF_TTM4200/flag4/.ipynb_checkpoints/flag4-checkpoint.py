import os
import base64

def main():
    print("Welcome to this flag creator!\nIn three simple steps, you will become one flag richer:)")
    input("Press Enter to continue...")
    step = input("Which step are you on? (Step 1, 2 or 3)")
    print(step)
    if step == "1":
        step1()
    elif step == "2":
        step2()
    elif step == "3":
        step3()
    else:
        print("Not correct input!")
        goodbye()

def step1():
    print("\nStep 1")
    print("Create a folder with the name 'flagCreator'")
    ans = input("\nHave you already created a folder? (y/n)")
    if(ans == "n"):
        print("\nGood luck creating a folder")
        goodbye()
    elif ans == "y":
        if(os.path.isdir("flagCreator")):
            print("\nThe directory 'flagCreator' exists\nContinue to step 2")
            step2()
        else:
            print("\nThere is no directory with the name 'flagCreator'.\nTry again")
            exit()
    else:
        print("Not correct input!")
        goodbye()

def step2():
    print("\nStep 2")
    print("Inside the folder 'flagCreator', create a txt-file called 'myNewFlag'")
    ans = input("\nHave you already created a file? (y/n)")
    if(ans == "n"):
        print("\nGood luck creating a file")
        goodbye()
    elif ans == "y":
        if(os.path.isfile("flagCreator/myNewFlag.txt")):
            print("\nThe file 'myNewFlag.txt' exists\nContinue to step 3")
            step3()
            
        else:
            print("\nThere is no file with the name 'myNewFlag.\nTry again")
            exit()
    else:
        print("Not correct input!")
        goodbye()

def step3():
    print("\nStep 3")
    print("Inside the file 'myNewFlag.txt', write (one line):\n'Please, Mr. Robot! Give me the flag!'")
    ans = input("\nHave you already edited the file? (y/n)")
    if(ans == "n"):
        print("\nGood luck creating a file")
        goodbye()
    elif ans == "y":
        if(os.path.isfile("flagCreator/myNewFlag.txt")):
            try:
                with open("flagCreator/myNewFlag.txt") as file:
                    line = file.readline()
                    print(line)
                    if line == "Please, Mr. Robot! Give me the flag!\n" or line == "Please, Mr. Robot! Give me the flag!":
                        print("You have written the correct message")
                        winner()
                    else:
                        print("You have not written the correct message.\nPlease try again!")
                        goodbye()
            except IOError:
                print("File not accessible!")
        else:
            print("\nThere is no file with the name 'myNewFlag.\nTry again")
            exit()
    else:
        print("Not correct input!")
        goodbye()

def goodbye():
    print("Goodbye!")
    exit()

def winner():
    print("\nCongratulations!")
    print("You completed all the tasks. Here is the flag:")
    flag = "VFRNNDIwMHtXMDRIXzUxMFdfRDBXTl8wTl83SDNfQ3IzNDcxME59"
    decodeFlag = base64.b64decode(flag).decode()
    print(decodeFlag)

main()