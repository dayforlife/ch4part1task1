class Student():
    def __init__(self,name, last_name, year_of_entrance, department):
        self.name = name
        self.last_name = last_name
        self.year_of_entrance = year_of_entrance
        self.department = department
    
    def get_student_info(self):
        return f"{self.name} {self.last_name} поступил в {self.year_of_entrance} г. на факультет: {self.department} "

object1 = Student(
    "Вася", "Иванов", 2017, "IT"
)

print(object1.get_student_info())