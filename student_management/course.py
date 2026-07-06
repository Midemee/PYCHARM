class Course:
    def __init__(self, course_title, credit_unit, course_code, max_students):
        self.course_title = course_title
        self.credit_unit = credit_unit
        self.course_code = course_code
        self.max_students = max_students
        self.enrolled_students = []

    def register_student(self, student):
        if student in self.enrolled_students:
            raise ValueError('Student already registered')
        if self.is_full():
            raise ValueError('Course already full')
        self.enrolled_students.append(student)

    def remove_student(self, student):
        if student not in self.enrolled_students:
            raise ValueError('Student not enrolled in this course')
        self.enrolled_students.remove(student)

    def get_enrolled_students(self):
        return self.enrolled_students

    def get_available_slots(self):
        return self.max_students - len(self.enrolled_students)

    def is_full(self):
        return len(self.enrolled_students) >= self.max_students

    def get_course_title(self):
        return self.course_title

    def get_course_code(self):
        return self.course_code()

    def __str__(self):
        return (f"{self.course_code}: {self.course_title} "
                f"({len(self.enrolled_students)}/{self.max_students} enrolled)")