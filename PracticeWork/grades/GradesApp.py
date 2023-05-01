from PracticeWork.grades.StudentClass import *

students = []


def getinfo(student):
    print("Name: " + student.name)
    print("Current average: " + student.getgradeaverage())
    student.attendaverage()
    student.daysabsent()


def studentreport():
    print("Welcome!\nStudents:")








ant = Student('Anthony')
bonk = Student('Bianca')
jeb = Student("Jeb")
dave = Student("Dave")

students.extend([ant, bonk, jeb, dave])

ant.recordattendance('4/26', 'A')
ant.recordattendance('4/27', 'P')
ant.recordattendance('4/28', 'P')
ant.recordattendance('4/29', 'A')

bonk.recordattendance('4/26', 'A')
bonk.recordattendance('4/27', 'P')
bonk.recordattendance('4/28', 'P')
bonk.recordattendance('4/29', 'A')

jeb.recordattendance('4/26', 'A')
jeb.recordattendance('4/27', 'P')
jeb.recordattendance('4/28', 'P')
jeb.recordattendance('4/29', 'A')

dave.recordattendance('4/26', 'A')
dave.recordattendance('4/27', 'P')
dave.recordattendance('4/28', 'P')
dave.recordattendance('4/29', 'A')

ant.grades.extend([30, 10, 60])
bonk.grades.extend([50, 100, 80])
jeb.grades.extend([100, 92, 76])
dave.grades.extend([20, 89, 65])

for student in students:
    getinfo(student)
