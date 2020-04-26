from datetime import datetime

import person


class Student(person.Person):
    def __init__(self, name: str, age: int, surname: str, address: str,
                 telephone: str, email: str, courses: list, year_in_school: int):
        super(Student, self).__init__(self, name, age, surname, address)
        self.courses = courses
        self.year_in_school = year_in_school

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__course = courses

