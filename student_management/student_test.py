import unittest

from student_management.student import Student
from student_management.course import Course

class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Aramide Ashiwaju","mide@gmail.com","ST001","Computer Science")
        self.course1 = Course("Introduction to Programming",3,"CSC101",30)
        self.course2 = Course("Calculus I",3,"MTH102",30)
        self.course3 = Course("Physics I",2,"PHY103",30)

    def test_student_object_can_be_created(self):
        self.assertEqual("Aramide Ashiwaju", self.student.name)
        self.assertEqual("mide@gmail.com", self.student.email)
        self.assertEqual("ST001", self.student.student_id)
        self.assertEqual("Computer Science", self.student.department)
        self.assertEqual([], self.student.enrolled_courses)

    def test_student_can_enroll_in_a_course(self):
        self.student.enroll_course(self.course1)

        self.assertEqual(1, len(self.student.enrolled_courses))
        self.assertIn(self.course1, self.student.enrolled_courses)

    def test_student_cannot_enroll_in_same_course_twice(self):
        self.student.enroll_course(self.course1)
        with self.assertRaises(ValueError):
            self.student.enroll_course(self.course1)

    def test_student_can_drop_a_course(self):
        self.student.enroll_course(self.course1)
        self.student.drop_courses(self.course1)
        self.assertEqual(0, len(self.student.enrolled_courses))
        self.assertNotIn(self.course1, self.student.enrolled_courses)

    def test_student_cannot_drop_course_not_enrolled(self):
        with self.assertRaises(ValueError):
            self.student.drop_courses(self.course1)

    def test_student_can_record_grade_for_a_course(self):
        self.student.enroll_course(self.course1)
        self.student.record_grade(self.course1, 4.5)
        self.assertEqual(4.5, self.student.grades[self.course1])

    def test_student_cannot_record_grade_for_course_not_enrolled(self):
        with self.assertRaises(ValueError):
            self.student.record_grade(self.course1, 4.5)

    def test_student_can_calculate_gpa(self):
        self.student.enroll_course(self.course1)
        self.student.enroll_course(self.course2)
        self.student.enroll_course(self.course3)
        self.student.record_grade(self.course1, 4.0)
        self.student.record_grade(self.course2, 5.0)
        self.student.record_grade(self.course3, 3.0)
        self.assertEqual(4.0, self.student.calculate_gpa())

    def test_student_gpa_is_zero_when_no_grades_exist(self):
        self.assertEqual(0.0, self.student.calculate_gpa())

    def test_student_cannot_get_transcript_without_enrolled_courses(self):
        with self.assertRaises(ValueError):
            self.student.get_transcript()

    def test_student_can_get_transcript(self):
        self.student.enroll_course(self.course1)
        self.student.enroll_course(self.course2)
        self.student.record_grade(self.course1, 4.0)
        self.student.record_grade(self.course2, 5.0)
        transcript = self.student.get_transcript()
        self.assertEqual(
            {
                "CSC101": 4.0,
                "MTH102": 5.0
            },
            transcript
        )
