# https://leetcode.com/problems/relative-sort-array/

import unittest

from src.relative_sort_array import Solution

test_cases = [{"kwargs": {"arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], "arr2": [2, 1, 4, 3, 9, 6]}, "correct_output": [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]}, {"kwargs": {"arr1": [28, 6, 22, 8, 44, 17], "arr2": [22, 28, 8, 6]}, "correct_output": [22, 28, 8, 6, 17, 44]}]


class RelativeSortArray(unittest.TestCase):
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
