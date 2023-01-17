# https://leetcode.com/problems/strong-password-checker/

import unittest

from src.strong_password_checker import Solution

test_cases = [{"kwargs": {"password": "a"}, "correct_output": 5}, {"kwargs": {"password": "aA1"}, "correct_output": 3}, {"kwargs": {"password": "1337C0d3"}, "correct_output": 0}]


class StrongPasswordChecker(unittest.TestCase):
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
