from datetime import datetime


class Person:

    def __init__(self, name: str, age: int, surname: str, address: str,
                 telephone: str, email: str):
        self.name = name
        self.age = age
        self.surname = surname
        # self.birth_date(birth_date)
        self.address = address
        self.telephone = telephone
        self.email = email

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            self.__name = name

        @property
        def age(self):
            return self.__age

        @age.setter
        def name(self, age):
            self.__age = age