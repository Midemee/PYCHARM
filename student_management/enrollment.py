class Enrollment:

    def __init__(self, student, enrollment_id, course, grade, semester):
        self.student = student
        self.enrollment_id = enrollment_id
        self.course = course
        self.grade = grade
        self.semester = semester
        self.withdrawn = False

    def assign_grade(self, grade):
        self.grade = grade

    def update_grade(self, grade):
        self.grade = grade

    def view_enrollment(self):
        return {
            "student": self.student.name,
            "course": self.course.course_code,
            "grade": self.grade,
            "semester": self.semester
        }

    def is_passed(self):
        return self.grade >= 2.0

    def withdraw(self):
        self.withdrawn = True

    def __str__(self):
        return self.view_enrollment()