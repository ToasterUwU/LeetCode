# https://leetcode.com/problems/roman-to-integer/

import unittest

from src.roman_to_integer import Solution

test_cases = [{"kwargs": {"s": "III"}, "correct_output": 3}, {"kwargs": {"s": "LVIII"}, "correct_output": 58}, {"kwargs": {"s": "MCMXCIV"}, "correct_output": 1994}]


class RomanToInteger(unittest.TestCase):
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
