import student
import datetime


class Lecturer(student.Student):
    def __init__(self, name: str, surname: str, birth_date: datetime.date, address: str, person_id: int, courses: tuple,
                 study_year: int):
        super().__init__(name, surname, birth_date, address, person_id, courses, study_year)

    def teaches_something(self, stud: student.Student):
        pass

    def taught_students(self, students: list):
        pass