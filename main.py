from enum import Enum


class Role(Enum):
    STUDENT = "students"
    LECTURER = "lecturers"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.courses_attached:
                lecturer.courses_attached[course] += [grade]
            else:
                lecturer.courses_attached[course] = [grade]
        else:
            return "Ошибка"

    def calculate_average_grade(self):
        total_sum = 0
        total_count = 0
        for course_grades in self.grades.values():
            total_sum += sum(course_grades)
            total_count += len(course_grades)

        if total_count == 0:
            return 0
        return total_sum / total_count

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {round(self.calculate_average_grade(), 2)} \n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {', '.join(self.finished_courses)} \n")

    def __lt__(self, other):
        if self.calculate_average_grade() < other.calculate_average_grade():
            return True
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = {}

    def calculate_average_grade(self):
        total_sum = 0
        total_count = 0
        for course_grades in self.courses_attached.values():
            total_sum += sum(course_grades)
            total_count += len(course_grades)
        if total_count == 0:
            return 0
        return total_sum / total_count

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {round(self.calculate_average_grade(), 2)} \n")

    def __lt__(self, other):
        if self.calculate_average_grade() < other.calculate_average_grade():
            return True
        return False


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n")


def calculate_course_average(people, course, who):
    total_sum = 0
    total_count = 0
    if who == Role.STUDENT.value:
        for person in people:
            if course in person.grades:
                total_sum += sum(person.grades[course])
                total_count += len(person.grades[course])
    elif who == Role.LECTURER.value:
        for person in people:
            if course in person.courses_attached:
                total_sum += sum(person.courses_attached[course])
                total_count += len(person.courses_attached[course])
    else:
        return "Ошибка"
    if total_count == 0:
        return 0
    return round(total_sum / total_count, 2)

best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

other_student = Student('Steve', 'Jobs', 'man')
other_student.courses_in_progress += ['Python']
other_student.finished_courses += ['Введение в программирование']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

other_mentor = Reviewer('Elon', 'Musk')
other_mentor.courses_attached += ['Python']
other_mentor.courses_attached += ['Git']
other_mentor.courses_attached += ['Введение в программирование']


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, "Git", 9)
cool_mentor.rate_hw(other_student, "Python", 10)


good_lecturer = Lecturer("Ray", "Ban")
best_student.rate_lecturer(good_lecturer, 'Python', 10)
best_student.rate_lecturer(good_lecturer, 'Python', 7)

other_lecturer = Lecturer("Mark", "Zuckerberg")
other_student.rate_lecturer(other_lecturer, 'Python', 9)

for i in (best_student, other_student, good_lecturer, other_lecturer, cool_mentor, other_mentor):
    print(i)

if best_student < other_student:
    print(f"Лучший студент: {other_student.name} {other_student.surname}\n ")
else:
    print(f"Лучший студент: {best_student.name} {best_student.surname}\n ")

if good_lecturer < other_lecturer:
    print(f"Лучший лектор: {other_lecturer.name} {other_lecturer.surname}\n ")
else:
    print(f"Лучший лектор: {good_lecturer.name} {good_lecturer.surname}\n ")

print(f"Средняя оценка по курсу Python у студентов: {calculate_course_average([best_student, other_student], 'Python', Role.STUDENT.value)}\n ")

print(f"Средняя оценка по курсу Python у лекторов: {calculate_course_average([good_lecturer, other_lecturer], 'Python', Role.LECTURER.value)}\n ")