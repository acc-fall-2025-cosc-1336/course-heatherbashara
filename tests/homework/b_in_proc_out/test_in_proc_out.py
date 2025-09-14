import unittest
from src.homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_numbers_7x7(self):
        self.assertEqual(multiply_numbers(7, 7), 49)

    def test_multiply_numbers_5x5(self):
        self.assertEqual(multiply_numbers(5, 5), 25)

if __name__ == "__main__":
    unittest.main()
