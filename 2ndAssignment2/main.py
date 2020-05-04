import student
import lecturer
import course

lecturer1 = lecturer.Lecturer("prof", 'fessor', '1970,7,5', 'ramat hasharon', '08-6880255', 'scwartz123@gmail.com',
                              '8000', 'high', '200')
lecturer2 = lecturer.Lecturer("prof2", 'rfessor', '1978,1,5', 'ramat hasharon', '08-6880255', 'scwartz123@gmail.com',
                              '8009', 'high', '250')

python_course = course.Course("python", lecturer1)

js_course = course.Course("javaScript", lecturer2)


student1 = student.Student('מומצא', 'שורץ', '1989,6,13', 'petch tikva', '054-6472701'
                           , 'rahelsc@gmail.com', [python_course, js_course], 2)

student2 = student.Student('ronen', 'schwartz', '1988,6,14', 'petch tikva', '054-6472701'
                           , 'rahelsc@gmail.com', [js_course], 2)

student1.fname = 'rahel'
student1.birthdate = '1988,6,14'
# recalculation works only if called - as requested in the assignment
student1.calculate_age()

print(student1.__str__())


# def check_who_teaches(teacher: lecturer.Lecturer, s: student.Student):
#     try:
#         for i in teacher.teaches_courses:
#             for j in s.courses:
#                 if i == j:
#                     print(f'{teacher.fname} teaches {i}')
#                     print(f'{s.fname} studies {i}')
#     except TypeError:
#         print("only recieves a lecturer and a student, please try again")
#     except:
#         print("bad input, try again")


# Q2
print(f'{js_course.lecturer.fname} teaches javaScript')
for coursestudent in js_course.get_participants():
    print(coursestudent.fname, end=" ")
    if coursestudent != js_course.get_participants()[-1]:
        print('&', end=" ")

print(f'study {js_course.name}')

# Q3
print(student1.age)
