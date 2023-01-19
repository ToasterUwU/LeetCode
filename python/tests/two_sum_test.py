# https://leetcode.com/problems/two-sum/

import unittest

from src.two_sum import Solution

test_cases = [{"kwargs": {"nums": [2, 7, 11, 15], "target": 9}, "correct_output": [0, 1]}, {"kwargs": {"nums": [3, 2, 4], "target": 6}, "correct_output": [1, 2]}, {"kwargs": {"nums": [3, 3], "target": 6}, "correct_output": [0, 1]}]


class TwoSum(unittest.TestCase):
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
