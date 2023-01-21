# https://leetcode.com/problems/first-missing-positive/

import unittest

from src.first_missing_positive import Solution

test_cases = [{"kwargs": {"nums": [1, 2, 0]}, "correct_output": 3}, {"kwargs": {"nums": [3, 4, -1, 1]}, "correct_output": 2}, {"kwargs": {"nums": [7, 8, 9, 11, 12]}, "correct_output": 1}]


class FirstMissingPositive(unittest.TestCase):
    def test_leet_code_examples(self):
        solution_obj = Solution()
        func = [
            getattr(solution_obj, method)
            for method in dir(solution_obj)
            if callable(getattr(solution_obj, method)) and not method.startswith("_")
        ][0]

        for test_case in test_cases:
            self.assertEqual(func(**test_case["kwargs"]), test_case["correct_output"])


if __name__ == "__main__":
    unittest.main()
