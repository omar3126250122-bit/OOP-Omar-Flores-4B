class Student:
    def __init__(self,name):
        self.name = name

    def enroll(self,course):
        self.course = course

    def show_course(self):
        print(f"{self.name} is enrolled in {self.course}")

class Course:
    def __init__(self,name):
        self.name = name 

    def show(self):
        print(f"Course: {self.name}")

#Instances:
student = Student("Carlos")
course = Course("Python Programming")

#Creating relationship
student.enroll(course)

#Use the relationship
student.show_course()

#Output expected. "Carlos is enrolled in Python Programming"

