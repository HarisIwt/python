"""
10.3DN task
Student ID 537318
Haris Liang
Class Definition and Usage

"""


class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        if isinstance(name, str):
            self.name = name

        else:
            print("error type,the name should be a string type.\n")

        if isinstance(idNumber, int):
            self.idNumber = idNumber
        else:
            print("error type,the animal type should be a int type.\n")

        if isinstance(department, str):
            self.department = department
        else:
            print("error type,the department should be a str type.\n")

        if isinstance(jobTitle, str):
            self.jobTitle = jobTitle
        else:
            print("error type,the jobTitle should be a str type.\n")

    def setName(self, value):
        if isinstance(value, str):
            self.name = value
        else:
            print("error type,the name should be a string type.\n")

    def setIdNumber(self, value):
        if isinstance(value, int):
            self.idNumber = value
        else:
            print("error type,the id number should be a int type.\n")

    def setDepartment(self, value):
        if isinstance(value, str):
            self.department = value
        else:
            print("error type,the department should be a string type.\n")

    def setJobTitle(self, value):
        if isinstance(value, str):
            self.jobTitle = value
        else:
            print("error type,the job title should be a string type.\n")

    def getName(self):
        return self.name

    def getIdNumber(self):
        return self.idNumber

    def getDepartment(self):
        return self.department

    def getJobTitle(self):
        return self.jobTitle

    def printFormat(self):
        print("%s %d %s %s" % self.name, self.idNumber, self.department, self.jobTitle)
