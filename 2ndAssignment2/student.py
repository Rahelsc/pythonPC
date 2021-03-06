import person
import course


class Student(person.Person):
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email, courses: list, year):
        super().__init__(fname, lname, birthdate, adress, telephone, email)
        self.courses = courses
        self.year = year

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses
        for course_1 in courses:
            course_1.update_participants(self)
