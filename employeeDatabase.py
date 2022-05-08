"""
10.3DN task
Student ID 537318
Haris Liang
Class Definition and Usage

"""

from employee import Employee
from tabulate import tabulate

DarthVader = Employee("Darth Vader", 123456, "Empire", "Supreme Leader")
LukeSkywalker = Employee("Luke Skywalker", 246810, "Rebellion", "Red 5 Leader")
HanSolo = Employee("Han Solo", 135790, "Acquisitions", "Chief Smuggler")
LeiaOrgana = Employee("Leia Organa", 888888, "Royalty", "Princess")
Chewbacca = Employee("Chewbacca", 111112, "IT", "CTO")

f = [[DarthVader.name, DarthVader.idNumber, DarthVader.department, DarthVader.jobTitle],
     [LukeSkywalker.name, LukeSkywalker.idNumber, LukeSkywalker.department, LukeSkywalker.jobTitle],
     [HanSolo.name, HanSolo.idNumber, HanSolo.department, HanSolo.jobTitle],
     [LeiaOrgana.name, LeiaOrgana.idNumber, LeiaOrgana.department, LeiaOrgana.jobTitle],
     [Chewbacca.name, Chewbacca.idNumber, Chewbacca.department, Chewbacca.jobTitle]]

print(tabulate(f, headers=["Name", "ID Number", "Department", "Job Title"]))
