class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Студенты должны выставлять оценки лекторам
    def rate_course(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and\
                grade in range(0, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        str_course = ', '.join(self.courses_in_progress)
        str_course_end = ', '.join(self.finished_courses)
        res = "Имя: " + self.name + "\nФамилия: " + self.surname + "\nСредняя оценка за домашние задания: " + \
              self.average() + "\nКурсы в процессе изучения: " + str_course + "\nЗавершенные курсы: " + str_course_end
        return res

    def average(self):
        av = 0
        for k in self.grades.values():
            av = av + sum(k) / len(k)
        aver_grades = av / len(self.grades)
        return str(aver_grades)

    def __lt__(self, other):
        return self.average() > other.average()

    def average_cource(self, name_cource):
        grades_list = self.grades[name_cource]
        return sum(grades_list) / len(grades_list)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}  # для выставления оценок студентами лекторам. Ключ - курс, значение - список отценок

    def __str__(self):
        res = "Имя: " + self.name + "\nФамилия: " + self.surname + "\nСредняя оценка за лекции: " + self.average()
        return res

    def average(self):
        av = 0
        for k in self.grades.values():
            av = av + sum(k) / len(k)
        aver_grades = av / len(self.grades)
        return str(aver_grades)

    def __lt__(self, other):
        return self.average() > other.average()

    def average_cource(self, name_cource):
        grades_list = self.grades[name_cource]
        return sum(grades_list) / len(grades_list)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = "Имя: " + self.name + "\nФамилия: " + self.surname
        return res


def common_average(list_students, name_cource):
    sum_grade = 0
    i = 0
    for ls in list_students:
        if name_cource in ls.grades.keys():
            sum_grade = sum_grade + ls.average_cource(name_cource)
            i = i + 1
    return sum_grade / i


def common_average_lecturers(list_lecturers, name_cource):
    sum_grade = 0
    lec = 0
    for ll in list_lecturers:
        if name_cource in ll.grades.keys():
            sum_grade = sum_grade + ll.average_cource(name_cource)
            lec = lec + 1
    return sum_grade / lec


some_student = Student('Roy', 'Eman', 'male')
some_student.courses_in_progress += ['Python', 'Git']
some_student.add_courses('Введение в программирование')

some_student1 = Student('Jek', 'Run', 'male')
some_student1.courses_in_progress += ['Java', 'Git']
some_student1.add_courses('Введение в программирование')

list_st = [some_student1, some_student]

some_reviewer = Reviewer('Li', 'Speed')
some_reviewer.courses_attached += ['Python', 'Java']
some_reviewer1 = Reviewer('Arni', 'Big')
some_reviewer1.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Java', 5)
some_reviewer.rate_hw(some_student, 'Java', 6)

some_reviewer1.rate_hw(some_student, 'Git', 1)
some_reviewer1.rate_hw(some_student, 'Git', 3)
some_reviewer1.rate_hw(some_student1, 'Git', 4)
some_reviewer1.rate_hw(some_student1, 'Git', 9)

print(common_average(list_st, 'Python'))

some_lecturer = Lecturer('Alex', 'Murzin')
some_lecturer2 = Lecturer('Dan', 'Onix')

some_lecturer.courses_attached += ['Git']
some_lecturer2.courses_attached += ['Git', 'Python']

list_ll = [some_lecturer, some_lecturer2]

some_student.rate_course(some_lecturer, 'Git', 1)
some_student.rate_course(some_lecturer, 'Git', 2)
some_student.rate_course(some_lecturer2, 'Git', 3)
some_student.rate_course(some_lecturer2, 'Git', 10)
some_student.rate_course(some_lecturer2, 'Python', 9)
some_student.rate_course(some_lecturer2, 'Python', 9)

some_student1.rate_course(some_lecturer, 'Git', 5)
some_student1.rate_course(some_lecturer, 'Git', 7)
some_student1.rate_course(some_lecturer2, 'Git', 8)
some_student1.rate_course(some_lecturer2, 'Git', 1)

print(common_average_lecturers(list_ll, 'Git'))
print(common_average_lecturers(list_ll, 'Python'))

some_mentor = Mentor('Lis', 'Cody')
some_mentor1 = Mentor('Frank', 'Star')

print(some_reviewer)
print(some_student1.grades)
print(some_student.grades)
print(some_lecturer)

print(some_student1 > some_student)
