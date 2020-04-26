import datetime  # we will use this for date objects


class Person:

    def __init__(self, name: str, surname: str, birth_date: datetime.date, address: str, person_id: int):
        self.__name = name
        self.__surname = surname
        self.__birth_date = birth_date
        self.__address = address
        # self.__telephone = telephone
        # self.__email = email
        self.__id = person_id

    def __str__(self):
        return f'שמי הפרטי הוא:{self.__name}' \
               f'-----' \
               f' שם משפחתי הוא:{self.__surname}' \
               f'-----' \
               f' אני גר(ה) ב:{self.__address}'

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year

        if today < datetime.date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1

        return age

    # just for simplifying the output, in general there should be 2 functions :)
    @property
    def name(self):
        return self.__name + ' ' + self.__surname

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

