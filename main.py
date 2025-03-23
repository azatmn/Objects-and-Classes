class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def RatingForLecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
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
                f"Средняя оценка за домашние задания: {self.calculate_average_grade()} \n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {', '.join(self.finished_courses)} \n")

    def __lt__(self, other):
        if self.calculate_average_grade() < other.calculate_average_grade():
            return f"{other.name} {other.surname}"
        else:
            return f"{self.name} {self.surname}"


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
                f"Средняя оценка за лекции: {self.calculate_average_grade()} \n")

    def __lt__(self, other):
        if self.calculate_average_grade() < other.calculate_average_grade():
            return f"{other.name} {other.surname}"
        else:
            return f"{self.name} {self.surname}"


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n")


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


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, "Git", 9)
cool_mentor.rate_hw(other_student, "Python", 10)


good_lecturer = Lecturer("Ray", "Ban")
best_student.RatingForLecturer(good_lecturer, 'Python', 10)
best_student.RatingForLecturer(good_lecturer, 'Python', 7)

other_lecturer = Lecturer("Mark", "Zuckerberg")
other_student.RatingForLecturer(other_lecturer, 'Python', 10)

for i in (best_student, other_student, good_lecturer, other_lecturer, cool_mentor):
    print(i)

print(f"Лучший студент: {best_student < other_student}\n ")

print(f"Лучший лектор: {good_lecturer < other_lecturer}")