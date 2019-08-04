##############################################
# Name: Angel Moreta
# Assignment: final project
# Purpose: shows employees currently on the system
# you can also look for their name, last name or id
# note: n/a
##############################################

import final_project
import csv


# constant
LIST_ALL = '1'
LIST_BY_DEPT = '2'
LOOK_UP_NAME = '3'
LOOK_UP_ID = '4'
QUIT = '0'

def main():
    # empty list
    employees = []
    # pass by Reference and append objects
    readFile(employees)
    # display maainmenu() and store choice
    choice = mainMenu()

    while choice in ['1','2','3','4']:
        if choice == LIST_ALL: # if one call listAll(list)
            print()             # funct to show employees
            listAll(employees)
            choice = mainMenu() # display menu again
        if choice == LIST_BY_DEPT: # if two call listAllByDept(list)
            print()                # show employees by dept
            listAllByDept(employees)
            choice = mainMenu()
        if choice == LOOK_UP_NAME: # if three call getByName(list and a name)
            name = input('\t Enter name to search: ').capitalize()
            matches = getByName(employees, name)
            print()
            if matches != []:  # if theres a match display it!
                for match in matches:
                    match.printObject()
            else:
                print(f'\t{name} was not found')
            choice = mainMenu()
        if choice == LOOK_UP_ID: # if four search by id(list and idnum)
            eid = input('\tEnter employee id to search: ')
            employee_inf = getByID(employees, eid)
            if employee_inf != 0:
                employee_inf.printObject()
            else:
                print(f'\t{eid} not found!')
            choice = mainMenu()

# getByID accepts a list of objects and
# a ID number to look for, then returns obj
def getByID(employees, id):
    for emp_obj in employees:
        id_inf = emp_obj.getEmployeeID()
        try:
            if int(id) == id_inf:
                return emp_obj
        except ValueError:
            return 0
    return 0

# getByName accepts a list of objects and
# a name to look for, then returns obj
def getByName(employees,name):
    emp_lst = []
    for match in employees:
        if name == match.getFirstName() or name == match.getLastName():
            emp_lst.append(match)
        if name == '':
            emp_lst.clear()
    return emp_lst

def listAllByDept(employees):
    tempEmployee = sorted(employees, key=lambda x: x.getDeparment())
    for department in tempEmployee:
        department.printObject()

def listAll(employees):
    for emp_inf in employees:
        emp_inf.printObject()

def add_new_empl():
    pass        

# mainMenu displays a menu of choices
def mainMenu():
    print('\nMAIN MENU')
    print('=' * 50)
    print('1: List all Employees')
    print('2: List all Employees by Department')
    print('3: Find Employee by name')
    print('4: Find Employee by ID')
    print('5: Add New Employee')
    print('Anything else quit()')
    choice = input('choice option: ')
    return choice

# read file and fill a list up with
# employee objects
def readFile(employees):
    # open file with and read  w csv.reader()
    with open('employees.csv','r') as i:
        emp_file = csv.reader(i)
        # count var to control objects
        count = 1
        # loop through each line of the file
        for emp in emp_file:
            # modify as it is looping
            emp = ' '.join(emp).replace('  ',' ')
            emp = emp.split()
            x = emp.pop(-1)
            y = emp.pop(-1)
            if emp[-1].isalpha():
                z = emp.pop(-1)
                emp.append(z + ' ' + y + ' ' + x)
                if emp[-1].isalpha():
                    w = emp.pop()
                    emp.append(w + ' ' + z + ' ' + y + ' ' + x)
            else:
                emp.append(y + ' ' + x)
            if len(emp) == 6:
                y = emp.pop()
                x = emp.pop()
                z = x + ' ' + y
                emp.append(z)

            # create employee obj list
            emp_obj = final_project.Employee(emp[0],emp[1],
                                            emp[2],emp[3],
                                            emp[4],)
            # append to the list that it
            # was passed as a reference
            employees.append(emp_obj)



main()
