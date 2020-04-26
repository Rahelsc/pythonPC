from datetime import datetime

import employee


class Lecturer(employee.Employee):
    def __init__(self, name: str, age: int, surname: str, birth_date, address: str,
                 telephone: str, email: str, base_salary: str, seniority: str, rate_per_hour: int):
        super().__init__(name, age, surname, birth_date, address, telephone, email, base_salary,
                         seniority)
        self.rate_per_hour = rate_per_hour

    @property
    def rate_per_hour(self):
        return self.__rate_per_hour

    @rate_per_hour.setter
    def rate_per_hour(self, rate_per_hour):
        self.__rate_per_hour = rate_per_hour
