import unittest
from student_management.student import Student
from student_management.course import Course

class CourseTest(unittest.TestCase):

    def setUp(self):
        self.course = Course("Introduction to Programming",3,"CSC101",2)
        self.student1 = Student("Aramide Ashiwaju","john@gmail.com","ST001","Computer Science")
        self.student2 = Student("kate Johnson","jane@gmail.com","ST002","Software Engineering")
        self.student3 = Student("Mike Adenuga","mike@gmail.com","ST003","Cyber Security")

    def test_course_object_can_be_created(self):
        self.assertEqual(
            "Introduction to Programming",
            self.course.course_title
        )
        self.assertEqual(3, self.course.credit_unit)
        self.assertEqual("CSC101", self.course.course_code)
        self.assertEqual(2, self.course.max_students)
        self.assertEqual([], self.course.enrolled_students)

    def test_course_can_register_a_student(self):
        self.course.register_student(self.student1)
        self.assertEqual(1, len(self.course.enrolled_students))
        self.assertIn(self.student1, self.course.enrolled_students)

    def test_student_cannot_register_twice(self):
        self.course.register_student(self.student1)
        with self.assertRaises(ValueError):
            self.course.register_student(self.student1)

    def test_course_can_remove_a_student(self):
        self.course.register_student(self.student1)
        self.course.remove_student(self.student1)
        self.assertEqual(0, len(self.course.enrolled_students))
        self.assertNotIn(self.student1, self.course.enrolled_students)

    def test_cannot_remove_student_not_registered(self):
        with self.assertRaises(ValueError):
            self.course.remove_student(self.student1)

    def test_course_can_return_all_enrolled_students(self):
        self.course.register_student(self.student1)
        self.course.register_student(self.student2)
        students = self.course.get_enrolled_students()
        self.assertEqual(2, len(students))
        self.assertIn(self.student1, students)
        self.assertIn(self.student2, students)

    def test_new_course_has_no_enrolled_students(self):
        self.assertEqual([], self.course.get_enrolled_students())

    def test_course_can_return_available_slots(self):
        self.course.register_student(self.student1)
        self.assertEqual(1, self.course.get_available_slots())

    def test_new_course_has_all_available_slots(self):
        self.assertEqual(2, self.course.get_available_slots())

    def test_new_course_is_not_full(self):
        self.assertFalse(self.course.is_full())

    def test_available_slots_becomes_zero_when_course_is_full(self):
        self.course.register_student(self.student1)
        self.course.register_student(self.student2)
        self.assertEqual(0, self.course.get_available_slots())

    def test_course_knows_when_it_is_full(self):
        self.course.register_student(self.student1)
        self.course.register_student(self.student2)
        self.assertTrue(self.course.is_full())

    def test_cannot_register_student_when_course_is_full(self):
        self.course.register_student(self.student1)
        self.course.register_student(self.student2)
        with self.assertRaises(ValueError):
            self.course.register_student(self.student3)
