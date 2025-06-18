class GradeBook:
    def __init__(self):
        self.students = {}  
    
    def add_student(self, name, grade):
        self.students[name] = grade
    
    def calculate_average(self):
        total = sum(self.students.values())
        return total / len(self.students)
    
    def display_grades(self):
        print("\nStudent Grades:")
        for name, grade in self.students.items():
            print(f"{name}: {grade}")
        print(f"\nClass Average: {self.calculate_average():.2f}")


if __name__ == "__main__":

    math_class = GradeBook()
    
    math_class.add_student("Alice", 88)
    math_class.add_student("Bob", 92)
    math_class.add_student("Charlie", 76)
    math_class.add_student("Diana", 85)
    

    math_class.display_grades()
