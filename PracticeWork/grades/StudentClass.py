class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = {}
        self.grades = []

    def daysabsent(self):
        absences = ""
        for day in self.attendance.keys():
            if self.attendance.get(day).lower() == "a":
                absences += day + ", "
        print("Absences:" + absences)

    def recordattendance(self, date, value):
        self.attendance.update({date: value})

    def attendaverage(self):
        total_days = len(self.attendance)
        absences = 0
        if len(self.attendance) == 0:
            print("Attendance average: No attendance info for this student.")
            return
        for val in self.attendance.values():
            if val.lower() == "a":
                absences += 1
        average = (total_days - absences) / total_days * 100
        print("Attendance average: " + str(average) + "%")

    def addgrade(self, grade):
        self.grades.append(grade)


def getgradeaverage(student):
    grade_total = 0
    for grade in student.grades:
        grade_total += grade
    return str(round(grade_total / len(student.grades), 2))

# ant = Student('Anthony')
#
# ant.recordattendance('4/26', 'A')
# ant.recordattendance('4/27', 'P')
# ant.recordattendance('4/28', 'P')
# ant.recordattendance('4/29', 'A')
#
# ant.addgrade(50)
# ant.addgrade(100)
# ant.addgrade(80)
#
# ant.daysabsent()
#
# ant.attendaverage()
#
# print(ant.getgradeaverage())