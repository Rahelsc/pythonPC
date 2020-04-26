import person
import datetime  # we will use this for date objects
import lecturer


class Student(person.Person):
    def __init__(self, name: str, surname: str, birth_date: datetime.date, address: str, person_id: int, courses: tuple,
                 study_year: int):
        super().__init__(name, surname, birth_date, address, person_id)
        self.__courses = courses
        self.__year = study_year

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def takes_courses(self):
        pass

    def takes_courses_from(self, martse: lecturer.Lecturer):
        pass
