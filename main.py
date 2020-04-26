import datetime  # we will use this for date objects
import person
import student
import lecturer
# import worker

p = person.Person(
    "שירלי",
    "משולם",
    datetime.date(1992, 3, 12),  # year, month, day
    "רח' שבי בשקט 13",
    #"012 12345678",
    #"sh.meshulam@example.com",
    123456
)
print('tst')
#  p.__name = 'whatewer2'
print(p.name())
#  print(p.__email)
print(p.age())

student1 = student.Student("Muhammad", "Ben-Ami", datetime.date(1990, 1, 11)
                           , "Some street 13 at Some City", 15,
                           ('Python','Java'),
                           2020)
student2 = student.Student("Iris", "York", datetime.date(1982, 4, 16)
                           , "Some street 14 at Some City", 16, ('Python','C#'), 2020)
student1.takes_courses()
student2.takes_courses()

lecturer1 = lecturer.Lecturer('Whoever','Ben-Zakkai',datetime.date(1979, 1, 3)
                              , 'Some addr',19, ('Python','Advanced Algorithms'), 2020)

if lecturer1.teaches_something(student1) :
    print(f"{lecturer1.name()} {lecturer1.surname()} teaches {student1.takes_courses_from(lecturer1)}")

print(f"{student1.name()} and {student2.name()} study {lecturer1.taught_students(student1, student2)} from {lecturer1.name()}")
