class Student:
    def __init__(self, name, email, student_id, department):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.department = department
        self.enrolled_courses = []
        self.grades = {}

    def enroll_course(self, course):
        if course in self.enrolled_courses:
            raise ValueError("Course already enrolled")
        self.enrolled_courses.append(course)

    def drop_courses(self, course):
        if course not in self.enrolled_courses:
            raise ValueError("Course not enrolled")
        self.enrolled_courses.remove(course)

    def record_grade(self, course, grade):
        if course not in self.enrolled_courses:
            raise ValueError("Course not enrolled, cannot grade")
        self.grades[course] = grade

    def calculate_gpa(self):
        if len(self.grades) == 0:
            return 0.0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def get_transcript(self):
        if len(self.enrolled_courses) == 0:
            raise ValueError("No courses enrolled")
        transcript = {}
        for course, grade in self.grades.items():
            transcript[course.course_code] = grade
        return transcript

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.department}"