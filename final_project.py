##############################################
# Name: Angel Moreta
# Assignment: final project class
# Purpose:
# note: n/a
##############################################

class Employee():
    # initialize
    def __init__(self,fname,lname, eid, dept, title):
        self.__firstName = str(fname)
        self.__lastName = str(lname)
        self.__employeeID = int(eid)
        self.__department = int(dept)
        self.__title = str(title)

    # display 
    def printObject(self):
        print('\t',self.__firstName,end=', ')
        print(self.__lastName,end=', ')
        print(self.__employeeID,end=', ')
        print(self.__department,end=', ')
        print(self.__title)


    # return inst
    def getDeparment(self):
        return self.__department
    def getEmployeeID(self):
        return self.__employeeID
    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
