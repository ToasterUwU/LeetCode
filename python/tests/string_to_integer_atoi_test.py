# https://leetcode.com/problems/string-to-integer-atoi/

import unittest

from src.string_to_integer_atoi import Solution

test_cases = [{"kwargs": {"s": "42"}, "correct_output": 42}, {"kwargs": {"s": "   -42"}, "correct_output": -42}, {"kwargs": {"s": "4193 with words"}, "correct_output": 4193}]


class StringToIntegerAtoi(unittest.TestCase):
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
