# https://leetcode.com/problems/longest-valid-parentheses/

import unittest

from src.longest_valid_parentheses import Solution

test_cases = [{"kwargs": {"s": "()(())"}, "correct_output": 6}, {"kwargs": {"s": "()"}, "correct_output": 2}, {"kwargs": {"s": "(()"}, "correct_output": 2}, {"kwargs": {"s": ")()())"}, "correct_output": 4}, {"kwargs": {"s": ""}, "correct_output": 0}]


class LongestValidParentheses(unittest.TestCase):
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
