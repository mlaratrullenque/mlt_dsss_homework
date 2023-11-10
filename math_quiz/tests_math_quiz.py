import unittest
from math_quiz import random_integer, random_operation, create_problem


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        # Test if the random operation is one of the expected operations
        for _ in range(1000):  # Test a large number of random values
            rand_op = random_operation()
            self.assertIn(rand_op, ['+', '-', '*'])

    def test_create_problem(self):
        test_cases = [
            #sum 
            (5, 2, '+', '5 + 2', 7),
            #multiplication
            (8, 3, '*', '8 * 3', 24),
            #substraction 
            (10, 4, '-', '10 - 4', 6),
            #substraction with negative result
            (8, 9, '-', '8 - 9', -1)
            
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
