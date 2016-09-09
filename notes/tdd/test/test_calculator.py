import unittest
from app.calculator import Calculator   # how?

# pylint: disable=R0904
# Locally disabling too-many-public-methods (R0904)
class TddInPythonExample(unittest.TestCase):

    def setUp(self):        # setUp() and tearDown() defined in unittest
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2) # must be self.x otherwise not found
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_error_if_x_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_error_if_y_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')

if __name__ == '__main__':
    unittest.main()         # standard unittest runner
