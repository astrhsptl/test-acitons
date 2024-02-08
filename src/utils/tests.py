from django.test import TestCase

from services.some import subtraction

class AnimalTestCase(TestCase):
    def setUp(self):
        self.testable_function = subtraction

    def test_subtraction(self):
        subtraction_result = self.testable_function(3, 2)

        self.assertEqual(subtraction_result, 3)