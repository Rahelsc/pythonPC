from builtins import property
from datetime import datetime, date


class Person:
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.adress = adress
        self.telephone = telephone
        self.email = email
        today = date.today()
        self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                                   self.birthdate.day))

    def __str__(self):
        return f'שמי הפרטי הוא:{self.fname}' \
               f'-----' \
               f' שם משפחתי הוא: {self.lname}' \
               f'-----' \
               f' אני גרה ב{self.adress}'

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def birthdate(self):
        return self.__birthdate

    # noinspection PyAttributeOutsideInit
    @birthdate.setter
    def birthdate(self, birthdate):
        try:
            year, month, day = map(int, birthdate.split(','))
            self.__birthdate = datetime(year, month, day)
            return self.__birthdate
        except ValueError:
            print("פורמט לא תואם, נסה שוב")

    def calculate_age(self):
        today = date.today()
        self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                                   self.birthdate.day))
        return self.age

