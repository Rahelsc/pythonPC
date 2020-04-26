import person


class Employee(person.Person):
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email, base_salary, seniority):
        super().__init__(fname, lname, birthdate, adress, telephone, email)
        self.base_salary = base_salary
        self.seniority = seniority
