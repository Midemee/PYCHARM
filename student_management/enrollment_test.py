import unittest
from student_management.student import Student
from student_management.course import Course
from student_management.enrollment import Enrollment

class EnrollmentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Mide Ashiwaju","mide@gmail.com","ST001","Computer Science")
        self.course = Course("Introduction to Programming",3,"CSC101",30)
        self.enrollment = Enrollment(self.student,"EN001",self.course,0.0,"First Semester")

    def test_enrollment_object_can_be_created(self):
        self.assertEqual(self.student, self.enrollment.student)
        self.assertEqual("EN001", self.enrollment.enrollment_id)
        self.assertEqual(self.course, self.enrollment.course)
        self.assertEqual(0.0, self.enrollment.grade)
        self.assertEqual("First Semester", self.enrollment.semester)
        self.assertFalse(self.enrollment.withdrawn)

    def test_enrollment_can_assign_grade(self):
        self.enrollment.assign_grade(4.5)
        self.assertEqual(4.5, self.enrollment.grade)

    def test_enrollment_can_update_grade(self):
        self.enrollment.assign_grade(3.0)
        self.enrollment.update_grade(4.5)
        self.assertEqual(4.5, self.enrollment.grade)

    def test_can_view_enrollment_details(self):
        self.enrollment.assign_grade(4.5)

        details = self.enrollment.view_enrollment()

        self.assertEqual(
            {
                "student": "Mide Ashiwaju",
                "course": "CSC101",
                "grade": 4.5,
                "semester": "First Semester"
            },
            details
        )

    def test_student_passes_course(self):
        self.enrollment.assign_grade(3.5)
        self.assertTrue(self.enrollment.is_passed())

    def test_student_fails_course(self):
        self.enrollment.assign_grade(1.5)
        self.assertFalse(self.enrollment.is_passed())

    def test_enrollment_can_be_withdrawn(self):
        self.enrollment.withdraw()
        self.assertTrue(self.enrollment.withdrawn)
