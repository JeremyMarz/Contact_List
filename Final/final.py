#========================================================
#Jeremy Martinez
#12/4/2019
#Final Project
#Description: Contact List
#========================================================
import re
import sys
import os

personList = []
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

class Person:
    """ This is the Person class that we use to be our Person object"""
    firstName = ""
    lastName = ""
    number = ""
    email = ""
    
    def __init__(self, firstName, lastName, number, email):
        self.firstName = firstName
        self.lastName = lastName
        self.number = str(number)
        self.email = str(email)


def addPerson():
    """addPerson function gets user input and adds person to list"""

    firstName = input("Please type the persons first name.\n")
    lastName = input("Please type the persons last name.\n")
    print("Please type the persons phone number.")
    phone = sys.stdin.readline().strip()
    validate = re.compile(r'^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$')
    if not validate.search(phone):
        print("Invalid number, try again.")
        addPerson()
    print("Please type the persons email.")
    email = sys.stdin.readline().strip()
    if(re.search(regex,email)):
        pass
    else:
        print("Invalid Email, try again.")
        addPerson()

    personList.append(Person(firstName, lastName, phone,email))
    main()


def deletePerson():
    """ deletePerson deletes the person with the last name as specified by the user"""

    if not personList:
        print("================================================")
        print("List is empty.")
        main()

    lastName = input("Please type the persons last name of whom you'd like to delete. Or type main to return to menu. \n")
    for person in personList:
        if(person.lastName == lastName):
            personList.remove(person)
            print("Deletion successful.")
            main()
            pass
        elif(lastName == "main"):
             main()
             pass
    print("Person not found.")
    deletePerson()


def findPerson():
    """ gets user input and finds person by last name and then displays thier information"""
    if not personList:
        print("================================================")
        print("List is empty.")
        main()

    lastName = input("Please type the persons last name of whom you'd like to find and display. Or type main to return to menu.\n")
    for person in personList:
        if(person.lastName == lastName):
            print(person.firstName+" "+person.lastName+" "+person.number+" "+person.email)
            main()
            pass
        elif(lastName == "main"):
             main()
             pass
    print("Person not found.")
    findPerson()


def listAll():
    """ listAll list all people in our list"""

    if not personList:
        print("================================================")
        print("List is empty.")
        main()

    print("================================================")
    print("List")
    print("================================================")
    personList.sort(key=lambda x: x.lastName)
    for person in personList:
        print(person.firstName+" "+person.lastName+" "+person.number+" "+person.email)
    main()

def load():
    """ load creates a list of people out of our text file"""

    with open('contacts.txt', "r") as contacts:
        lines = contacts.readlines()
        for line in lines:  
            cur = line.split(',') 
            personList.append(Person(cur[1], cur[0], cur[2],cur[3].strip()))


def main():
    """ main displays menu and operates user actions"""

    print("================================================")
    print("Main Menu")
    print("A - Add Person")
    print("D - Delete Person")
    print("F - Find and Display Person")
    print("L - List All People")
    print("S - Save List")
    print("E - Exit")
    print("================================================\n")
    var = input("Enter Choice:\n")
    if(var == 'A' or var == 'a'):
        addPerson()
    elif(var == 'D' or var == 'd'):
        deletePerson()
    elif(var == 'F' or var == 'f'):
        findPerson()
    elif(var == 'L' or var == 'l'):
        listAll()
    elif(var == 'S' or var == 's'):
        save()
    elif(var == 'E' or var == 'e'):
        exit()

def save():
    """ save, saves our list to the text document"""

    with open('contacts.txt', 'w') as contacts:
        for person in personList:
                addition = person.lastName+","+person.firstName+","+person.number+","+person.email+"\n"
                contacts.write(addition)
    print("================================================\n")
    print("List saved.")

    main()

load()
main()
