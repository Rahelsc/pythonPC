import person


class Student(person.Person):
    def __init__(self, name, age, surname, address, telephone, email, courses, year_in_school):
        super(Student, self).__init__(self, name, age, surname, address, telephone, email)
        self.courses = courses
        self.year_in_school = year_in_school

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__course = courses


new_student = Student('name', 32, 'surname', 'address', 'telephone', 'email', 'courses', 5)
print(new_student.name)
