from datetime import datetime
import person


class Employee(person.Person):
    def __init__(self, name: str, age: int, surname: str, birth_date, address: str,
                 telephone: str, email: str, base_salary: int, seniority: str):
        super().__init__(name, age, surname, birth_date, address, telephone, email)
        self.base_salary = base_salary
        self.seniority = seniority

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, base_salary):
        self.__base_salary = base_salary
