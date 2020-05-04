class Course:

    def __init__(self, name, lecturer):
        self.students = []
        self.name = name
        self.lecturer = lecturer

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lecturer(self):
        return self.__lecturer

    @lecturer.setter
    def lecturer(self, lecturer):
        self.__lecturer = lecturer

    def update_participants(self, student):
        self.students.append(student)

    def get_participants(self):
        return self.students
