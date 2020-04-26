import student



student1 = Student('מומצא', 'שורץ', '1989,6,13', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'js'], 2)

student2 = Student('ronen', 'schwartz', '1988,6,14', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'cSharp'], 2)

lecturer1 = Lecturer("prof", 'fessor', '1970,7,5', 'ramat hasharon', '08-6880255', 'scwartz123@gmail.com', '8000',
                     'high'
                     , '200', ['python'])

student1.fname = 'רחל'
student1.birthdate = '1988,6,14'
# works only if called - as requested in the assignment
student1.calculate_age()


print(student1.__str__())


def check_who_teaches(teacher: Lecturer, s: Student):
    try:
        for i in teacher.teaches_courses:
            for j in s.courses:
                if i == j:
                    print(f'{teacher.fname} teaches {i}')
                    print(f'{s.fname} studies {i}')
    except TypeError:
        print("only recieves a lecturer and a student, please try again")
    except:
        print("bad input, try again")


check_who_teaches(lecturer1, student1)

print(student1.age)