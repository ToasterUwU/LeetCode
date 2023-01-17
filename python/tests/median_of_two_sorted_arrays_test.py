# https://leetcode.com/problems/median-of-two-sorted-arrays/

import unittest

from src.median_of_two_sorted_arrays import Solution

test_cases = [{"kwargs": {"nums1": [1, 3], "nums2": [2]}, "correct_output": 2.0}, {"kwargs": {"nums1": [1, 2], "nums2": [3, 4]}, "correct_output": 2.5}]


class MedianOfTwoSortedArrays(unittest.TestCase):
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
