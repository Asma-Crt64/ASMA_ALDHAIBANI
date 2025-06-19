class student:
    name=""
    grade=0
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def avg(self, studentList):
        total = 0
        for student in studentList:
            total += student.grade 
        return total / len(studentList)  

s1 = student("Bob", 67)
s2 = student("Anas", 90)
s3 = student("Sarah", 89)

studentList = [s1, s2, s3]
average = s1.avg(studentList)  
print(f"The average grade is: {average:.2f}")  
