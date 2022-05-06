"""
10.2CR task
Student ID 537318
Haris Liang
Class Definition

"""


class Animal:
    def __init__(self, name, animalType, age, adopted):
        if isinstance(name, str):
            self.name = name
        else:
            print("error type,the name should be a string type.\n")

        if isinstance(animalType, str):
            self.animalType = animalType
        else:
            print("error type,the animal type should be a string type.\n")

        if isinstance(age, int):
            self.age = age
        else:
            print("error type,the animal age should be a int type.\n")

        if isinstance(adopted, bool):
            self.adopted = adopted
        else:
            print("error type,the adopted should be a boolean type.\n")

    def setName(self, value):
        if isinstance(value, str):
            self.name = value
        else:
            print("error type,the name should be a string type.\n")

    def setAnimalType(self, value):
        if isinstance(value, str):
            self.animalType = value
        else:
            print("error type,the animal type should be a string type.\n")

    def setAge(self, value):
        if isinstance(value, int):
            self.age = value
        else:
            print("error type,the animal age should be a int type.\n")

    def setAdopted(self, value):
        if isinstance(value, bool):
            self.adopted = value
        else:
            print("error type,the adopted should be a boolean type.\n")

    def getName(self):
        return self.name

    def getAnimalType(self):
        return self.animalType

    def getAge(self):
        return self.age

    def getAdopted(self):
        return self.adopted

    def __str__(self):  # print all elements
        print("name = %s animalType = %s age = %d adopted = %r" % (self.name, self.animalType, self.age, self.adopted))
