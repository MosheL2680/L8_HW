import json
import os


# clear terminal when runing program
def clear():
    os.system("cls")
    

# get first n last name from user, put it into a dictionary
def get():
    firstName = input("inter your first name")
    lastName = input("inter your last name")
    global userName
    userName = {"first name": firstName, "last name": lastName}    


# save the dictionary into a JSON file
def save():
    with open("userName.json", "w") as json_file:
        json.dump(userName, json_file)


# read from the json file and put it into a new dictionary
def read():
    with open("userName.json", "r") as json_file:
        global userNameFromJson
        userNameFromJson = json.load(json_file)


# print in green the dictionary i just loaded
def printInGreen():
    print("\033[32m", userNameFromJson, "\033[0m")
